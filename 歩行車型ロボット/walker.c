
#include	<stdio.h>
#include	<fcntl.h>
#include	<time.h>
#include	<termios.h>
#include	<string.h>
#include    <stdlib.h>
#include 	<sys/types.h>
#include 	<sys/stat.h>
#include 	<sys/ioctl.h>
#include 	<unistd.h>
#include 	<pthread.h>
#include 	<zmq.h>
#include 	<assert.h>

#define true        	1
#define false			0
#define comNo_right 	0	//右側力覚センサCOMナンバー
#define comNo_left  	1	//左側力覚センサCOMナンバー
#define comNo_arduino 	0	//Arduino Due COMナンバー
#define sr          	100 //サンプリング周波数
#define NUM_THREAD 		2	//スレッド数
#define PATH_SIZE 512

#define MAX_BUF 64
unsigned int value;

//定数定義
double M = 50, D = 50, SMasatsuF = 0.1, DMasatsuK = 0.05, Gravity=9.80665, gain=1.11, Body_weight=70.0;

const unsigned int sync_gpio = 78;
//摩擦を考慮したモード
const int f_mode = 0; //0のときは摩擦考慮しない
int DS_mode = 0; //0のときは静止摩擦力、1のときは動摩擦力
//校正用
double			mean_right[6], mean_left[6];//校正用の平均

//変数定義
int				status;
int				fdc_right, fdc_left;
int				fdc_arduino;
char			devname_right[64], devname_left[64], devname_arduino[64];
char			str_right[256], str_left[256], str_arduino[2048];//生文字データ用
unsigned short	data_right[6], data_left[6];//数値データ用
double  sum_data_right[6], sum_data_left[6];
int				tick;
int				clk;
int				n_right, n_left, n_arduino;
double			p_force_right[6], p_force_left[6], now_force_right[6], now_force_left[6];//前の力，今の力
double			total_force[6];//合力，合計トルク
double			dt;//サンプリング周期
FILE			*fp;//書き込みファイル用
double			sens_right[6] = {12.924, 13.376, -13.160, 649.500, 657.300, 650.100};
double			sens_left[6] = {13.218, 13.154, -13.080, 656.000, 653.400, 658.000};
double      	g1 = 0, g2 = 0;
double      	x = 0, v = 0;
double 			f;
double 			voltage=0;
int 			m_voltage;
int 			FR = 0; //正転か逆転か
int				recv_cmd = 0; //コマンドが来たか判別
char			fileName[128];
char			comment[64];
char			year_month_day[64];
char			csv_dir[64];
char 			currDir[PATH_SIZE];
struct stat 	statBuf;

double 			t;
struct timespec t_p;
struct timespec t_a;
int				i = 0;
double 			t_i=0;//インターバル時間
long			encoder_val=0, *e;

//プロトタイプ宣言
int SetComAttr(int fdc);
int SetComAttr2(int fdc);
void waitSampleTime(void);
void waitSampleTime_2(double dt);//Test用
void* socketConnectionFunc(void* arg);
void* readEncoderFunc(void* arg);
int Read_Force(void);
int Calib_Force(int ct);
int sum_Right_Left(void);
int getVoltageOutput(void);
void measuring(void);

void getDate(void);
double time_diff(struct timespec *start, struct timespec *end);

//メイン処理
int main(){

	// COMポートをオープン
	sprintf(devname_right, "/dev/ttyUSB%d", comNo_right);
	sprintf(devname_left, "/dev/ttyUSB%d", comNo_left);
	sprintf(devname_arduino, "/dev/ttyACM%d", comNo_arduino);

	//それぞれのシリアルデバイスのファイルディスクリプタを定義
	fdc_right = open(devname_right, O_RDWR | O_NOCTTY | O_NONBLOCK);
	fdc_left = open(devname_left, O_RDWR | O_NOCTTY | O_NONBLOCK);
	fdc_arduino = open(devname_arduino, O_RDWR | O_NOCTTY | O_NONBLOCK);

	if (fdc_arduino < 0) {
        printf("Arduinoと接続されていません。終了します。\n");
		printf("%d", fdc_right);
        return -1;
    }
	//サンプリング周期
	dt = (double)1/sr;

	// COMポートのボーレート等を設定
	SetComAttr(fdc_right); //921.6kbit/s
	SetComAttr(fdc_left); //921.6kbit/s
	SetComAttr2(fdc_arduino); //115.2kbit/s

	//ソケット通信のスレッドを立てる
	pthread_t t[NUM_THREAD];
    pthread_create(&t[0], NULL, socketConnectionFunc, NULL);
	pthread_create(&t[1], NULL, readEncoderFunc, NULL);

	//試行当日の日時取得
	getDate();

	//カレントディレクトリ取得
	getcwd(currDir, PATH_SIZE);

	//実験当日のフォルダがあるか確認．なかったら作成．
	sprintf(csv_dir, "%s%s%s", currDir, "/logs/", year_month_day);

	if (stat(csv_dir, &statBuf) != 0){

		mkdir(csv_dir, 0777);
	}

	//メインループ
	while(true){
		switch (recv_cmd)
		{
		case 0:
			//待機状態
			printf("waiting\n");
			sleep(1);
			break;

		case 1:
			//キャリブレーションモード
			printf("Mode:Calibration\n");
			sleep(1);//ZMQのスレッドとメインルーチンは非同期のため，パラメータ格納のために時間が必要
			Calib_Force(10);
			recv_cmd = 0;
			break;

		case 2:
			//計測モード

			printf("Mode:Measuring\n");
			sleep(1);//ZMQのスレッドとメインルーチンは非同期のため，パラメータ格納のために時間が必要
			measuring();

			recv_cmd = 0;

			break;

		case 3:
			//デバッグモード
			printf("dubugging....\n");

			sleep(1);

		default:
			break;
		}
	}
}

/**** 以下，宣言関数 ****/

//ボーレート設定関数
int SetComAttr(int fdc){

	int			n;
	struct termios	term;
	// ボーレート等を設定
	n = tcgetattr(fdc, &term);
	bzero(&term, sizeof(term));
	term.c_cflag = B921600 | CS8 | CLOCAL | CREAD;
	term.c_iflag = IGNPAR;
	term.c_oflag = 0;
	term.c_lflag = 0;/*ICANON;*/
	term.c_cc[VINTR]    = 0;     /* Ctrl-c */
	term.c_cc[VQUIT]    = 0;     /* Ctrl-? */
	term.c_cc[VERASE]   = 0;     /* del */
	term.c_cc[VKILL]    = 0;     /* @ */
	term.c_cc[VEOF]     = 4;     /* Ctrl-d */
	term.c_cc[VTIME]    = 0;
	term.c_cc[VMIN]     = 0;
	term.c_cc[VSWTC]    = 0;     /* '?0' */
	term.c_cc[VSTART]   = 0;     /* Ctrl-q */
	term.c_cc[VSTOP]    = 0;     /* Ctrl-s */
	term.c_cc[VSUSP]    = 0;     /* Ctrl-z */
	term.c_cc[VEOL]     = 0;     /* '?0' */
	term.c_cc[VREPRINT] = 0;     /* Ctrl-r */
	term.c_cc[VDISCARD] = 0;     /* Ctrl-u */
	term.c_cc[VWERASE]  = 0;     /* Ctrl-w */
	term.c_cc[VLNEXT]   = 0;     /* Ctrl-v */
	term.c_cc[VEOL2]    = 0;     /* '?0' */
//	tcflush(fdc, TCIFLUSH);
	n = tcsetattr(fdc, TCSANOW, &term);

	}

int SetComAttr2(int fdc){

	int			n;
	struct termios	term;
	// ボーレート等を設定
	n = tcgetattr(fdc, &term);
	bzero(&term, sizeof(term));
	term.c_cflag = B115200 | CS8 | CLOCAL | CREAD;
	term.c_iflag = IGNPAR;
	term.c_oflag = 0;
	term.c_lflag = 0;/*ICANON;*/
	term.c_cc[VINTR]    = 0;     /* Ctrl-c */
	term.c_cc[VQUIT]    = 0;     /* Ctrl-? */
	term.c_cc[VERASE]   = 0;     /* del */
	term.c_cc[VKILL]    = 0;     /* @ */
	term.c_cc[VEOF]     = 4;     /* Ctrl-d */
	term.c_cc[VTIME]    = 0;
	term.c_cc[VMIN]     = 0;
	term.c_cc[VSWTC]    = 0;     /* '?0' */
	term.c_cc[VSTART]   = 0;     /* Ctrl-q */
	term.c_cc[VSTOP]    = 0;     /* Ctrl-s */
	term.c_cc[VSUSP]    = 0;     /* Ctrl-z */
	term.c_cc[VEOL]     = 0;     /* '?0' */
	term.c_cc[VREPRINT] = 0;     /* Ctrl-r */
	term.c_cc[VDISCARD] = 0;     /* Ctrl-u */
	term.c_cc[VWERASE]  = 0;     /* Ctrl-w */
	term.c_cc[VLNEXT]   = 0;     /* Ctrl-v */
	term.c_cc[VEOL2]    = 0;     /* '?0' */
//	tcflush(fdc, TCIFLUSH);
	n = tcsetattr(fdc, TCSANOW, &term);
	}

double time_diff(struct timespec *start, struct timespec *end){
    return (double)(end->tv_sec - start->tv_sec) + (double)(end->tv_nsec - start->tv_nsec)/1000000000;
}

void waitSampleTime_2(double dt){

	while (true){

		/* clk = clock() / (CLOCKS_PER_SEC/1000) - clk0; */
		clock_gettime(CLOCK_MONOTONIC_RAW, &t_a);
		t_i = time_diff(&t_p, &t_a);
		if (t_i >= dt){
			t = t + dt;
			break;
		}
	}
}

///////ここでMDなどのパラメータを送信している

void* socketConnectionFunc(void* arg){
   //  Socket to talk to clients
    void *context = zmq_ctx_new ();
    void *responder = zmq_socket (context, ZMQ_REP);
    int rc = zmq_bind (responder, "tcp://*:5555");
    assert (rc == 0);

    while (1) {
        char payload [32];
		char UI_sendbuff[128];
		char head;
		char termi;
        zmq_recv (responder, payload, 32, 0);
        //printf ("Received\n");

		if(payload[0]=='a'){
			sscanf(payload, "%c,%d,%lf,%lf,%s,%c", &head, &recv_cmd, &M, &D, comment, &termi);
			printf("%d,%lf,%lf,%s\n", recv_cmd, M, D, comment);
			zmq_send (responder, "Robot:Received a", 16, 0);
		}else if(payload[0]=='b'){
			sprintf(UI_sendbuff, "%lf,%lf,%lf,%lf,%lf,%d,%ld,\n", total_force[1], *mean_left, *mean_right, t, v, m_voltage,encoder_val);
			zmq_send (responder, UI_sendbuff, sizeof(UI_sendbuff), 0);
		}

	}
    return NULL;
}

void* readEncoderFunc(void* arg){
    while (1) {
        n_arduino = read(fdc_arduino, str_arduino, sizeof(str_arduino));
		usleep(5000);
	}
    return NULL;
}

//力覚値読み取り関数
int Read_Force(void){

	// 単データリクエスト
	write(fdc_right, "R", 1);
	write(fdc_left, "R", 1);

	// 単データを得る
	n_right = read(fdc_right, str_right, 27);
	n_left = read(fdc_left, str_left, 27);

	//16進数データを各変数に代入
	sscanf(str_right, "%1d%4hx%4hx%4hx%4hx%4hx%4hx",
			&tick, &data_right[0], &data_right[1], &data_right[2], &data_right[3], &data_right[4], &data_right[5]);
	sscanf(str_left, "%1d%4hx%4hx%4hx%4hx%4hx%4hx",
			&tick, &data_left[0], &data_left[1], &data_left[2], &data_left[3], &data_left[4], &data_left[5]);

	//16進数から10進数へデコード
	sprintf(str_right, "%05lf,%d,%05d,%05d,%05d,%05d,%05d,%05d\n",
		clk / dt * dt, tick,
		data_right[0], data_right[1], data_right[2], data_right[3], data_right[4], data_right[5]);

	sprintf(str_left, "%05lf,%d,%05d,%05d,%05d,%05d,%05d,%05d\n",
		clk / dt * dt, tick,
		data_left[0], data_left[1], data_left[2], data_left[3], data_left[4], data_left[5]);

}

//キャリブレーション用関数
int Calib_Force(int ct){

	printf("キャリブレーション開始\n");
	//ファイル名
	sprintf(fileName, "%s%c%s%s%s", csv_dir, '/', "calib_",comment, ".csv");
	fp = fopen(fileName, "w");
	fprintf(fp, "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n",
			"time[s]", "Right_Force_x[N]", "Right_Force_y[N]", "Right_Force_z[N]", "Right_Moment_x[Nm]", "Right_Moment_y[Nm]", "Right_Moment_z[Nm]",
			"Left_Force_x[N]", "Left_Force_y[N]", "Left_Force_z[N]", "Left_Moment_x[Nm]", "Left_Moment_y[Nm]", "Left_Moment_z[Nm]");

	//変数の初期化
	for(int i=0; i<=5; i++){
		sum_data_right[i] = 0;
		sum_data_left[i] = 0;
	}

	i = 1;

	//指定した秒数データを取得する
	for(int i=1; i<=sr*ct; i++){
		clock_gettime(CLOCK_MONOTONIC_RAW, &t_p);

		Read_Force();
		//printf("%s%hd\n", "右の力（x）は、", data_right[0]);

		//和を求める
		for(int j=0; j<=5; j++){
			sum_data_right[j] += data_right[j];
			sum_data_left[j] += data_left[j];

		}
		//Excelファイル書き込み
		fprintf(fp, "%f,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d\n",
			t, data_right[0], data_right[1], data_right[2],
			data_right[3], data_right[4], data_right[5],
			data_left[0], data_left[1], data_left[2],
			data_left[3], data_left[4], data_left[5]);

		// サンプリング周期だけ待つ
		waitSampleTime_2(dt);
	}
	//平均を求める
	for(int i=0; i<=5; i++){
		mean_right[i] = sum_data_right[i] / (sr*ct);
		mean_left[i] = sum_data_left[i] / (sr*ct);
	}

	printf("キャリブレーション完了\n");
	printf("%s%lf%s\n","キャリブレーションに", t, "秒かかりました。");
	printf("%s%lf\n", "右の力（y）の合計は、", sum_data_right[1]);
	printf("%s%lf\n", "右の力（y）の合計は、", sum_data_right[1]);
	printf("%s%lf\n", "右の平均力（y）", mean_right[1]);
	printf("%s%lf\n", "左の平均力（y）", mean_left[1]);

	fclose(fp);
	recv_cmd = 0;
}

//合力計算関数
int sum_Right_Left(void){

	for(int i=0; i<=5; i++){
		total_force[i] = now_force_right[i] + now_force_left[i];

	}
}

//ルンゲクッタ用関数
double f1(double t, double x, double v) {
	double area = v;
	//printf("%lf\n", area);
	return area;
}

double f2(double f, double t, double x, double v) {
	double area = (f - D * v) / M;
	return area;
}
//出力電圧演算関数
int getVoltageOutput(){
	double k1, k2, k3, k4, h1, h2, h3, h4;

	/* if(total_force[1]<=0){
		total_force[1] = -total_force[1];
	} */

	if(f_mode == 1){
		if(DS_mode == 0){
			if(total_force[1] >=0 && total_force[1] < Body_weight*SMasatsuF*Gravity){
				FR = 4;
				v = 0;
				voltage = 0;
				return v;

			}else if(total_force[1] < 0 && total_force[1] >  -1*Body_weight*SMasatsuF*Gravity){
				FR = 4;
				v = 0;
				voltage = 0;
				return v;
			}
			else{
				DS_mode = 1;
			}

		}else{
			if(total_force[1] >=0){
				f = total_force[1]-Body_weight*Gravity*DMasatsuK;

			}else{
				f = total_force[1]+Body_weight*Gravity*DMasatsuK;

			}

			if(total_force[1] >=0 && total_force[1] <= Body_weight*Gravity*DMasatsuK){
				DS_mode = 0;

			}
			if(total_force[1] < 0 && total_force[1] > -Body_weight*Gravity*DMasatsuK){
				DS_mode = 0;

			}
		}

	}else{
			f = total_force[1];
			/* if(f<5){
				f = 0;
			} */
		}

	k1 = dt * f1(t, x, v);
	h1 = dt * f2(f, t, x, v);

	//printf("t \n");
	//printf("%lf\n", t);
	//printf("x \n");
	//printf("%lf\n", x);
	//printf("v \n");
	//printf("%lf\n", v);


	k2 = dt * f1(t + dt / 2.0, x + h1 / 2, v + h1 / 2);
	h2 = dt * f2(f, t + dt / 2.0, x + h1 / 2, v + h1 / 2);

	k3 = dt * f1(t + dt / 2.0, x + h2 / 2, v + h2 / 2);
	h3 = dt * f2(f, t + dt / 2.0, x + h2 / 2, v + h2 / 2);

	k4 = dt * f1(t + dt / 2.0, x + h3 / 2, v + h3 / 2);
	h4 = dt * f2(f, t + dt / 2.0, x + h3 / 2, v + h3 / 2);

	x = g1 + (k1 + 2 * k2 + 2 * k3 + k4) / 6;
	v = g2 + (h1 + 2 * h2 + 2 * h3 + h4) / 6;

	//次の処理用に格納
	g1 = x;
	g2 = v;

	voltage =gain* v * (900/ (850 * 3.1415926535 * 0.1475));

	FR=0;
	if(voltage<0){
		voltage = -voltage;
		FR=1;
	}
}

void measuring(void){
	//ファイル名（FSTWなど）
	sprintf(fileName, "%s%c%s%s", csv_dir, '/', comment, ".csv");
	printf("%s", comment);

	//ファイルを開く
	fp = fopen(fileName, "w");
	fprintf(fp, "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n",
			"interval [s]","time[s]", "Right_Force_x[N]", "Right_Force_y[N]", "Right_Force_z[N]", "Right_Moment_x[Nm]", "Right_Moment_y[Nm]", "Right_Moment_z[Nm]",
			"Left_Force_x[N]", "Left_Force_y[N]", "Left_Force_z[N]", "Left_Moment_x[Nm]", "Left_Moment_y[Nm]", "Left_Moment_z[Nm]",
			"Force_x[N]", "Force_y[N]", "Force_z[N]", "Moment_x[Nm]", "Moment_y[Nm]", "Moment_z[Nm]",
			"Vo[V]", "Synchronization", "direction of rotation", "Velocity [m/s]","1Encoder[counts]");

	//Arduinoへの送信用バッファを確保
	char sendbuf[64];
	//Arduinoへの受信用バッファを確保
	FR = 3;
	m_voltage = 0;
	sprintf(sendbuf, "%d,%d", FR, m_voltage);
	//Arduinoシリアルポートに開始コマンドを送る
	write(fdc_arduino, sendbuf, sizeof(sendbuf));
	//変数初期化
	i = 1;
	x = 0, v = 0, t = 0;

	while(1){
		//ループの開始時間を格納
		clock_gettime(CLOCK_MONOTONIC_RAW, &t_p);

		//Arduinoへの送信用バッファを確保
		char sendbuf[32];
		//Arduinoへの受信用バッファを確保
		char recvbuf[16];
		//Encoder用文字配列
		char enc_str[16]; //エンコーダ値

		int len_recvbuf = 0;

		//力覚値読み取り
		Read_Force();

		//力覚値を格納
		for(int i=0; i<=5; i++){
			now_force_right[i] = ((double)data_right[i] - mean_right[i]) / sens_right[i];
			now_force_left[i] = ((double)data_left[i] - mean_left[i]) / sens_left[i];
		}

		//合力計算
		sum_Right_Left();

		//エラーハンドル
		if((fabs(total_force[1]) > (double)200) && (t >= 1)){
			printf("Error: 200 [N]以上の力が検出されました．\nプログラムを終了します.");

			fclose(fp);
			close(fdc_arduino);
			close(fdc_left);
			close(fdc_right);
			exit(EXIT_FAILURE);
		}

		//出力電圧演算
		getVoltageOutput();

		//double型を送るのがめんどかったので，10000倍にしてバッファに格納
		m_voltage = (int)(voltage*10000);
		sprintf(sendbuf, "%d,%d", FR, m_voltage);

		//Arduinoシリアルポートに送信
		write(fdc_arduino, sendbuf, sizeof(sendbuf));

		//終端文字送信
		write(fdc_arduino, "\n", 1);

		//Arduinoからエンコーダ情報を読み取る
		while(true){
			char recvbuf[16];
			//Encoder用文字配列
			//char enc_str[16]; //エンコーダ値

			int start_byte = 0;
			int stop_byte = 0;

			len_recvbuf = read(fdc_arduino, recvbuf, sizeof(recvbuf));

			for(i=0; i<sizeof(enc_str); i++){
				enc_str[i] = '\0';
			}

			if(len_recvbuf==0){
				continue;
			}

			if(recvbuf[0] != 's'){
				continue;
			}
			recvbuf[strlen(recvbuf)] = '\0';
			for(i=1; i<(int)strlen(recvbuf)-1; i++){
				enc_str[i-1] = recvbuf[i];
			}
			enc_str[i-1] = '\0';
			encoder_val = strtol(enc_str, &e, 10);

			//printf("%s,%s,%d,%d\n", recvbuf, enc_str, (int)strlen(recvbuf),i);
			break;

		}
		//enc_val = atoi(recvbuf);

		//Excelファイル書き込み
		fprintf(fp, "%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%u,%d,%lf,%s\n",
				t_i, t, now_force_right[0], now_force_right[1], now_force_right[2],
					now_force_right[3], now_force_right[4], now_force_right[5],
					now_force_left[0], now_force_left[1], now_force_left[2],
					now_force_left[3], now_force_left[4], now_force_left[5],
					total_force[0], total_force[1], total_force[2],
					total_force[3], total_force[4], total_force[5],voltage,value,FR,v,enc_str);

		//ループ終了処理
		if(recv_cmd!=2)
		{
			fclose(fp);
			char sendbuf[32];
			m_voltage = 0, FR = 2;
			sprintf(sendbuf, "%d,%d", FR, m_voltage);
			write(fdc_arduino, sendbuf, sizeof(sendbuf));
			write(fdc_arduino, "\n", 1);
			break;
		}

		// サンプリング周期だけ待つ
		waitSampleTime_2(dt);
	}
}

void getDate(void){

    time_t 			timer;
    struct tm 		*date;

    timer = time(NULL);          /* 経過時間を取得 */
    date = localtime(&timer);    /* 経過時間を時間を表す構造体 date に変換 */

	strftime(year_month_day, 255, "%Y_%m_%d", date);
}