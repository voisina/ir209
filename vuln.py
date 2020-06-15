import socket
import sys
import os

def usage():
	print("Usage: python3 vuln.py [IP_ADDRESS_TO_BIND]")
	sys.exit(0)
	
if len(sys.argv) != 2:
	usage()
else:
	UDP_IP = sys.argv[1]

UDP_PORT = 8989

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

data_str = ""

while data_str !="stop":
	data, addr = sock.recvfrom(1024)
	data_str = data.decode("utf-8")
	#restrict command
	if "ls" not in data_str and "cat" not in data_str:
		print("Command forbidden")
	else:
		os.system(data_str)
	