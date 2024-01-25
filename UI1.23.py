# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
import sys
import time
import queue
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore, QtGui


from concurrent import futures

import logging
import threading

import grpc
import grpc_tuna_pb2
import grpc_tuna_pb2_grpc
import time

Vision_ip=''
Vision_port=''

RbPi1_ip=''
RbPi1_port=''

RbPi2_ip = ''
RbPi2_port =''

Scada_ip=''


form_class = uic.loadUiType("main.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.robot1_color_num=0
        self.robot2_weight=0
        self.robot3_weight=0
        self.red_count=0
        self.yellow_count=0
        self.green_count=0
        self.blue_count=0
        self.purple_count=0
        

        self.lcd_robot1.setProperty("value", self.robot1_color_num)
        self.lcd_robot2.setProperty("value", self.robot2_weight)
        self.lcd_robot3.setProperty("value", self.robot3_weight)

        self.lcd_10kg.setProperty("value", self.red_count)
        self.lcd_20kg.setProperty("value", self.yellow_count)
        self.lcd_30kg.setProperty("value", self.green_count)
        self.lcd_40kg.setProperty("value", self.blue_count)
        self.lcd_50kg.setProperty("value", self.purple_count)

        # self.lcd_kgline1.setProperty("value", self.pbar1)     #누적무게
        # self.lcd_kgline2.setProperty("value", self.pbar2)
        # self.lcd_kgline3.setProperty("value", self.pbar3)
        # self.lcd_kgline4.setProperty("value", self.pbar4)
        # self.lcd_kgline5.setProperty("value", self.pbar5)

        # self.lcd_slide1.setProperty("value", self.lcd_slide1_value)    #리스트 형태로 받아옴
        # self.lcd_slide2.setProperty("value", self.lcd_slide2_value)
        # self.lcd_slide3.setProperty("value", self.lcd_slide3_value)
        # self.lcd_slide4.setProperty("value", self.lcd_slide4_value)
        # self.lcd_slide5.setProperty("value", self.lcd_slide5_value)
        # self.lcd_slide6.setProperty("value", self.lcd_slide6_value)

        # self.bar_1.setProperty("value", self.pbar1_per)
        # self.bar_2.setProperty("value", self.pbar2_per)
        # self.bar_3.setProperty("value", self.pbar3_per)
        # self.bar_4.setProperty("value", self.pbar4_per)
        # self.bar_5.setProperty("value", self.pbar5_per)
        # # self.bar_1.setValue(self.pbar1)
        
        t1 = threading.Thread(target = self.Scada_RbPi1_client, args=(self,))
        t2 = threading.Thread(target = self.Scada_RbPi2_client, args=(self,))

        t1.start()
        t2.start()


    def Scada_RbPi1_client(self):
        channel = grpc.insecure_channel(f"{RbPi1_ip}:{RbPi1_port}")
        stub = grpc_tuna_pb2_grpc.DataStub(channel)

        try:
                grpc.channel_ready_future(channel).result(timeout=5)
                print("Success")  
        except grpc.FutureTimeoutError:
                print("Connection timeout.")
                return
        
        while True:
                try:
                        response = stub.Robot1_color(grpc_tuna_pb2.robot1_color())
                        self.robot1_now_color = response.now

                        if self.robot1_now_color == 'red':
                            self.robot1_color_num = 10
                        if self.robot1_now_color == 'yellow':
                            self.robot1_color_num = 20
                        if self.robot1_now_color == 'green':
                            self.robot1_color_num = 30
                        if self.robot1_now_color == 'blue':
                            self.robot1_color_num = 40
                        if self.robot1_now_color == 'purple':
                            self.robot1_color_num = 50
                        
                        response = stub.Count(grpc_tuna_pb2.Counts())
                        self.red_count = response.red
                        self.yellow_count = response.yellow
                        self.green_count = response.green
                        self.blue_count = response.blue
                        self.purple_count = response.purple
                                                        
                        #time.sleep(5)  # 일정 간격으로 요청
                except grpc.RpcError as e:
                        print(f"GRPC Error: {e}")
        
        #Scada_RbPi2_clinet thread    
    def Scada_RbPi2_client(self):
        channel = grpc.insecure_channel(f"{RbPi2_ip}:{RbPi2_port}")
        stub = grpc_tuna_pb2_grpc.DataStub(channel)

        try:
                grpc.channel_ready_future(channel).result(timeout=5)
                print("Success")  
        except grpc.FutureTimeoutError:
                print("Connection timeout.")
                return
        
        while True:
            try:
                response = stub.Remain(grpc_tuna_pb2.remain())
                self.remain_line1 = response.remain_line1
                self.remain_line2 = response.remain_line2
                self.remain_line3 = response.remain_line3
                self.remain_line4 = response.remain_line4
                self.remain_line5 = response.remain_line5

                response = stub.Maximum(grpc_tuna_pb2.maximum())
                self.maximum_line1 = response.maximum_line1
                self.maximum_line2 = response.maximum_line2
                self.maximum_line3 = response.maximum_line3
                self.maximum_line4 = response.maximum_line4
                self.maximum_line5 = response.maximum_line5

                response = stub.Robot2_weight(grpc_tuna_pb2.robot2_weight())
                self.robot2_weight = response.robot2_weight

                response = stub.Robot3_weight(grpc_tuna_pb2.robot3_weight())
                self.robot3_weight = response.robot3_weight

                response = stub.Slide_box(grpc_tuna_pb2.slide_weight())
                self.lcd_slide1_value = response.slide_1
                self.lcd_slide2_value = response.slide_2
                self.lcd_slide3_value = response.slide_3
                self.lcd_slide4_value = response.slide_4
                self.lcd_slide5_value = response.slide_5
                self.lcd_slide6_value = response.slide_6
                
                self.pbar1=self.maximum_line1-self.remain_line1
                self.pbar2=self.maximum_line2-self.remain_line2
                self.pbar3=self.maximum_line3-self.remain_line3
                self.pbar4=self.maximum_line4-self.remain_line4
                self.pbar5=self.maximum_line5-self.remain_line5
                self.pbar1_per = self.pbar1 / self.maximum_line1 * 100
                self.pbar2_per = self.pbar2 / self.maximum_line2 * 100
                self.pbar3_per = self.pbar3 / self.maximum_line3 * 100
                self.pbar4_per = self.pbar4 / self.maximum_line4 * 100
                self.pbar5_per = self.pbar5 / self.maximum_line5 * 100
                
            except grpc.RpcError as e:
                print(f"GRPC Error: {e}")

        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = WindowClass()
    ui.show()
    sys.exit(app.exec_())

    