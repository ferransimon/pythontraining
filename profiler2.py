# profiler2.py
# req/sec, short running request

from socket import *
from threading import Thread
import time

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 9000))

req = 0

def monit():
	global req
	while True:
		time.sleep(1)
		print(str(req)+" reqs/sec")
		req = 0

Thread(target=monit).start()

while True:
	sock.send(b'1')
	resp = sock.recv(100)
	req += 1