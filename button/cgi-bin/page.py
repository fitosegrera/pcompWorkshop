#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging in case of error
import cgitb
import serial
import time

cgitb.enable()

# Establish the connection on a specific serial port for the YUN
#s = serial.Serial('/dev/ttyATH0', 9600)
print "Content-type: text/html"
while True:
    print
    print "Hello World!"