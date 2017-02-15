# profiler1.py
# time profiler, long running request

from socket import *
import time

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 9000))

while True:
	start = time.time()
	sock.send(b'30')
	resp = sock.recv(100)
	end = time.time()
	print(end-start)