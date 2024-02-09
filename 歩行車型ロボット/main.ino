#include <stdio.h>
//PWM周波数は20kHzにしている。デフォルトは1kHz
//ピンアサイン
#define pin_fwd 4          //Forwardピン
#define pin_rvs 5          //Reverseピン
#define pin_m0 6           //M0ピン
#define pin_stop 7         //Stopピン
#define pin_pwm 8          //PWMピン
#define pin_Enc_A 11       //エンコーダーA層
#define pin_Enc_B 12       //エンコーダーB層
#define pin_InfraredLED 13 //赤外線LEDピン
#define pin_GRF 14         //GRF同期ピン
#define pin_EMG 16         //EMG同期ピン
#define pin_sw_AI 19       //スイッチ右に倒したとき
#define pin_sw_Robot 17    //スイッチ左に倒したとき
#define pin_camTrig 42     //UVCカメラトリガ信号ピン

#define PULSE_HIGH_TIME 40 //[us]
#define PHOTO_CYCLE 10000  //[us] //10 [ms]

//パルスジェネレータ用変数初期化
int pulse_count = 0;
unsigned long t, start_time, stop_time, now_clock[3];
char now_read[64];

//ロボット用変数初期化
volatile long encCount = 0; //必ずvolatile型にすること
volatile long preCount = 0; //必ずvolatile型にすること
volatile long encVel = 0; //必ずvolatile型にすること
String encPayload;

bool enc_start_flag = false;

int FR = 0; //正転：FR=0、逆転：FR=1
int duty = 0;
double vOut = 0;

//プロトタイプ宣言
void delayCycleTime(void);
void generatePulse(void);
void encItrA(void);
void encItrB(void);
inline void digitalWriteDirect(int pin, boolean val);
inline int digitalReadDirect(int pin);
int split(String data, char delimiter, String *dst);
void TC3_Handler();
void startTimer(Tc *tc, uint32_t channel, IRQn_Type irq, uint32_t mSec);

void setup()
{
  //ベアボーンとのシリアル通信開始
  Serial.begin(115200);
  //ピン設定
  pinMode(pin_fwd, OUTPUT);
  pinMode(pin_rvs, OUTPUT);
  pinMode(pin_m0, OUTPUT);
  pinMode(pin_stop, OUTPUT);
  pinMode(pin_camTrig, OUTPUT);
  pinMode(pin_InfraredLED, OUTPUT);
  pinMode(pin_Enc_A, INPUT_PULLUP);    //PULLUPにする必要あり
  pinMode(pin_Enc_B, INPUT_PULLUP);    //PULLUPにする必要あり
  pinMode(pin_sw_AI, INPUT_PULLUP);    //PULLUPにする必要あり
  pinMode(pin_sw_Robot, INPUT_PULLUP); //PULLUPにする必要あり
  pinMode(pin_EMG, OUTPUT);
  pinMode(pin_GRF, OUTPUT);

  //PWM出力を12bit対応に設定する。
  analogWriteResolution(12);

  //初期化
  digitalWrite(pin_camTrig, LOW);
  digitalWrite(pin_InfraredLED, LOW);

  digitalWrite(pin_fwd, LOW);
  digitalWrite(pin_rvs, HIGH);
  digitalWrite(pin_m0, LOW);
  digitalWrite(pin_stop, LOW);
  analogWrite(pin_pwm, 0);

  digitalWrite(pin_stop, HIGH);
  digitalWriteDirect(pin_EMG, LOW);
  digitalWriteDirect(pin_GRF, LOW);

  //Serial.println(digitalReadDirect(pin_sw_AI));
  //Serial.println(digitalReadDirect(pin_sw_Robot));

  //エンコーダ設定の有効化
  if (digitalReadDirect(pin_sw_AI)!=1){
    //エンコーダ読み取り関数始動
    attachInterrupt(pin_Enc_A, encItrA, CHANGE); //Aピンが変化した時itr_A()を呼び出す
    attachInterrupt(pin_Enc_B, encItrB, CHANGE); //Bピンが変化した時itr_B()を呼び出す
    //タイマー（シリアル通信用）
    //http://jtakao.web.fc2.com/elec/due_timerinterrupt/index.html
    //NVIC_SetPriority((IRQn_Type)SysTick_IRQn,1);  //microsなどの時間系統の優先順位を1に設定。
    NVIC_SetPriority((IRQn_Type)TC3_IRQn,1);  //TC3タイマーの優先順位を2に設定（普通は0なので優先度を下げたことになる）。エンコーダ読み取りを優先させるため。
    startTimer(TC1, 0, TC3_IRQn, 10);  //TC3タイマーを3msecに設定
    encCount = 0;
  }
}

void loop()
{
  if (digitalReadDirect(pin_sw_AI))
  {
    Serial.println("This is capture-mode");
    delay(5000);
    while (true)
    { 
      if(Serial.available()){
        now_read[0] = Serial.read();
        if (now_read[0] == 's')
        {
          //パルスカウンタを初期化
          pulse_count = 1;
          //開始時刻を記録
          start_time = micros();
          //赤外線LED発光と同時に、初回分のパルス送信
          digitalWriteDirect(pin_InfraredLED, HIGH); //digitalWrite(pin_InfraredLED, HIGH);
          //digitalWriteDirect(pin_GRF, HIGH);
          //digitalWriteDirect(start_stop_pin, LOW);
          //digitalWriteDirect(run_brake_pin, LOW);
          generatePulse();
          delayCycleTime();

          //2回目以降のパルス送信
          for (pulse_count = 2; pulse_count <= 20*(1000000/PHOTO_CYCLE); pulse_count++)
          {
            generatePulse();
            delayCycleTime();
          }
          digitalWriteDirect(pin_InfraredLED, LOW);
          stop_time = micros();
          //digitalWriteDirect(pin_GRF, LOW);
          //digitalWriteDirect(start_stop_pin, LOW);
          //digitalWriteDirect(run_brake_pin, HIGH);
          Serial.print("es");
          Serial.print(",");
          Serial.print(start_time);
          Serial.print(",");
          Serial.println(stop_time);

        }else if(now_read[0] == 'c'){
          //Serial.println("CCC");
          for(int i=0; i<=2; i++){
            now_clock[i] = micros();
            digitalWriteDirect(pin_GRF, HIGH);
            delay(2000);
            digitalWriteDirect(pin_GRF, LOW);
            delay(2000);
          }
          
          Serial.print("ec");
          Serial.print(",");
          Serial.print(now_clock[0]);
          Serial.print(",");
          Serial.print(now_clock[1]);
          Serial.print(",");
          Serial.println(now_clock[2]);

        }
        //delayMicroseconds(50);
      }
    }
  }
  else if (digitalReadDirect(pin_sw_Robot))
  {
    Serial.println("This is robot-mode");
    
    while (true)
    {
      String str;
      String payload[3] = {"\0"}; // 分割された文字列を格納する配列
      int raw_vol;                //電圧の10000倍の値
      //Serial.println(encCount);//エンコーダ値送信
      if (Serial.available())
      {
        //Serial.print(String(encCount));//エンコーダ値送信
        //終端文字まで読み込む
        str = Serial.readStringUntil('\n');
        //要素ごとに分解
        split(str, ',', payload);

        FR = payload[0].toInt();

        raw_vol = payload[1].toInt();
        vOut = (double)raw_vol / 10000;
        //Serial.println(vOut, 5);
        duty = vOut * (4096 / 3.3);
        //Serial.println(duty);
      }

      switch (FR)
      {
      case 0:
        digitalWriteDirect(pin_stop, HIGH);
        digitalWriteDirect(pin_fwd, LOW);
        delay(10);
        digitalWriteDirect(pin_rvs, HIGH);
        break;

      case 1:
        digitalWriteDirect(pin_stop, HIGH);
        digitalWriteDirect(pin_fwd, HIGH);
        delay(10);
        digitalWriteDirect(pin_rvs, LOW);
        break;

      case 2:
        digitalWriteDirect(pin_stop, LOW);
        digitalWriteDirect(pin_InfraredLED, LOW);
        digitalWriteDirect(pin_EMG, LOW);
        enc_start_flag = false;
        if(encPayload != ""){
          Serial.println(encPayload);
          encPayload = "";
        }
        encCount = 0;
        break;

      case 3:
        encPayload = "";
        encCount = 0;
        start_time = micros();
        enc_start_flag = true;
        digitalWriteDirect(pin_InfraredLED, HIGH);
        digitalWriteDirect(pin_EMG, HIGH);

        FR = 1;
        
        break;
      
      case 4:
        digitalWriteDirect(pin_stop, LOW);
        break;
      
      default:
        break;
      }

      analogWrite(pin_pwm, duty);
      //Serial.println(duty);
      //delay(10);
    }
  }
}

void delayCycleTime(void)
{
  while (true)
  {
    t = micros() - start_time;
    if (t >= pulse_count * PHOTO_CYCLE)
    {
      break;
    }
  }
}

void generatePulse(void)
{
  digitalWriteDirect(pin_camTrig, HIGH); //digitalWrite(pin_camTrig, HIGH);
  delayMicroseconds(PULSE_HIGH_TIME);
  digitalWriteDirect(pin_camTrig, LOW); //digitalWrite(pin_camTrig, LOW);
}

//エンコーダA相割り込み
void encItrA()
{
  encCount += digitalReadDirect(pin_Enc_A) == digitalReadDirect(pin_Enc_B) ? -1 : 1;
}
//エンコーダB相割り込み
void encItrB()
{
  encCount += digitalReadDirect(pin_Enc_A) == digitalReadDirect(pin_Enc_B) ? 1 : -1;
}
//digitalWrite高速化関数
inline void digitalWriteDirect(int pin, boolean val)
{
  if (val)
    g_APinDescription[pin].pPort->PIO_SODR = g_APinDescription[pin].ulPin;
  else
    g_APinDescription[pin].pPort->PIO_CODR = g_APinDescription[pin].ulPin;
}
//digitalRead高速化関数
inline int digitalReadDirect(int pin)
{
  return !!(g_APinDescription[pin].pPort->PIO_PDSR & g_APinDescription[pin].ulPin);
}

int split(String data, char delimiter, String *dst)
{
  int index = 0;
  int arraySize = (sizeof(data) / sizeof((data)[0]));
  int datalength = data.length();
  for (int i = 0; i < datalength; i++)
  {
    char tmp = data.charAt(i);
    if (tmp == delimiter)
    {
      index++;
      if (index > (arraySize - 1))
        return -1;
    }
    else
      dst[index] += tmp;
  }
  return (index + 1);
}

/**********タイマー用関数***************/
//http://jtakao.web.fc2.com/elec/due_timerinterrupt/index.htmlからのコピペ
//タイマーを使いやすくしてくれているらしい
void startTimer(Tc *tc, uint32_t channel, IRQn_Type irq, uint32_t mSec) {
  pmc_enable_periph_clk((uint32_t)irq);
  TC_Configure(tc, channel, TC_CMR_WAVE | TC_CMR_WAVSEL_UP_RC | TC_CMR_TCCLKS_TIMER_CLOCK1);
  uint32_t rc = (VARIANT_MCK/2/1000)*mSec;
  TC_SetRC(tc, channel, rc);
  TC_Start(tc, channel);
  tc->TC_CHANNEL[channel].TC_IER=TC_IER_CPCS;
  tc->TC_CHANNEL[channel].TC_IDR=~TC_IER_CPCS;
  NVIC_EnableIRQ(irq);
}

//タイマー割り込み
void TC3_Handler() {
  TC_GetStatus(TC1, 0);  //時間のカウントを0に戻す

  if(enc_start_flag){
    //Robotここから
    Serial.print('s');
    Serial.print(encCount);
    Serial.print('t');
    Serial.print('\0');
    //robotここまで

  }
}