#!/usr/bin/python
# -*- coding: utf-8 -*-

# pyduino
# Created by: fito_segrera 
# www.fii.to
# 10-1-14

import serial

s = serial.Serial('/dev/ttyATH0', 9600) #Establish the connection on a specific serial port for the YUN

while True:
    s.read(4)#number of received bytes