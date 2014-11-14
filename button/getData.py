#!/usr/bin/python
import urllib2
import serial
import time

s = serial.Serial('/dev/ttyATH0', 9600) #Establish the connection on a specific serial port for the YUN

while True:
    data = urllib2.urlopen("http://localhost:8000/cgi-bin/page.py").read()
    print "Received:", data
    s.write(chr(data))
    time.sleep(1)