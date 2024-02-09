# GUI関連

from PyQt5 import QtWidgets
from pyqtgraph.Qt import QtCore
import sys
import numpy as np
import ui
import zmq
import zmq.backend.cython
from zmq.backend import *

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui.Ui_Form()
        self.ui.setupUi(self)
        self.fps = 20
        self.gear = 30
        self.countPerRotation = 500*4 # 2000カウントで1回転

        # データを更新する関数を呼び出す時間を設定
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(int((1/self.fps)*1000))

        self.ui.graphicsView.setYRange(-50, 50)
        self.curve_force = self.ui.graphicsView.plot(pen=(255, 0, 100))
        self.data_force = np.zeros(200)

        self.ui.graphicsView_2.setYRange(-100000, 100000)
        self.curve_encoder = self.ui.graphicsView_2.plot(pen=(255, 0, 255))
        self.data_encoder = np.zeros(200)

        self.ui.graphicsView_3.setYRange(-50, 50)
        self.curve_rpm = self.ui.graphicsView_3.plot(pen=(255, 0, 255))
        self.data_rpm = np.zeros(200)

        self.preCount = 0
        self.rpm = 0

    ## ボタンがクリックされたら呼び出される関数
    def start_button_clicked(self):
        #デバッグ用プリント
        print("Start clicked")

        self.sendPacket("a", "2")
        print(socket.recv())

    def stop_button_clicked(self):
        print("Stop clicked")
        self.sendPacket("a", "0")
        print(self.recvPacket())


    def calib_button_clicked(self):
        print("Calib clicked")
        self.sendPacket(head="a", mode="1")
        print(self.recvPacket())

    ##MDのモードを変更する関数！！！
    def sendPacket(self, head, mode):
        if head == "a":

            mass = self.ui.lineEdit.text()
            dumper = self.ui.lineEdit_2.text()
            comment = self.ui.lineEdit_3.text()
            payload = head + "," + mode + "," + mass + "," + dumper + "," + comment + '\0'
            socket.send_string(payload)


        elif head == "b":
            socket.send_string(head)


    def recvPacket(self):

        message = socket.recv()
        return message.decode('utf-8',  "ignore")

    def calRpm(self, nowCount):
        rpm = ((((nowCount - self.preCount) * self.fps) / self.countPerRotation) * 60) / self.gear
        return rpm

    def update(self):
        self.sendPacket(head="b", mode=np.nan)

        payload = self.recvPacket()
        l = payload.split(',')
        self.ui.textBrowser.setText(l[3])
        self.ui.textBrowser_2.setText(str(int(float(l[2])/13.376)))
        self.ui.textBrowser_3.setText(str(int(float(l[1])/13.154)))
        self.ui.textBrowser_4.setText(l[0])
        self.ui.textBrowser_5.setText(l[4])
        self.ui.textBrowser_6.setText(str(float(l[5])/10000))
        self.ui.textBrowser_7.setText(l[6])
        self.ui.textBrowser_8.setText(str(self.calRpm(int(l[6]))))

        self.data_force = np.delete(self.data_force, 0)
        self.data_force = np.append(self.data_force, float(l[0]))
        self.curve_force.setData(self.data_force)

        self.data_encoder = np.delete(self.data_encoder, 0)
        self.data_encoder = np.append(self.data_encoder, int(l[6]))
        self.curve_encoder.setData(self.data_encoder)

        self.data_rpm = np.delete(self.data_rpm, 0)
        self.data_rpm = np.append(self.data_rpm, self.calRpm(int(l[6])))
        self.curve_rpm.setData(self.data_rpm)
        self.preCount = int(l[6])

if __name__ == '__main__':

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://172.22.16.177:5555")

    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    # main.MyFunc()
    main.show()
    sys.exit(app.exec_())