# example2.py
# Python concurrency

from socket import *
from threading import Thread
from concurrent.futures import ProcessPoolExecutor as Pool
from fib import fib

pool = Pool(4)

def high_cpu_usage_function(client):
	while True:
		req = client.recv(100)
		if not req:
			break
		fib_num = int(req)
		future = pool.submit(fib, fib_num)
		result = future.result()
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