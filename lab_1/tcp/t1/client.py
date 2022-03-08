# Basic TCP client
# Author: Srikar

import socket

HOST = "127.0.0.1"	# The server's hostname or IP address
PORT = 42069 		# The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	try:
		s.connect((HOST, PORT))
	except ConnectionRefusedError:
		print('Unable to connect to server, is the server running?')
		exit()

	server_data = s.recv(1024)
	s.sendall(b"I can hear you!")


print(f"Received: {server_data.decode()}")