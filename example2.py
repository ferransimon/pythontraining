# example2.py
# Python concurrency

from socket import *
from threading import Thread
from fib import fib

def high_cpu_usage_function(client):
	while True:
		req = client.recv(100)
		if not req:
			break
		fib_num = int(req)
		result = fib(fib_num)
		resp = str(result).encode('ascii') + b'\n'
		client.send(resp)

def server(address):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	sock.bind(address)
	sock.listen(5)
	while True:
		client, addr = sock.accept()
		print("Connection accepted", addr)
		Thread(target=high_cpu_usage_function, args=(client, )).start()

server(("", 9000))