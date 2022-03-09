# Basic UDP client
# Author: Srikar

import socket

HOST = "127.0.0.1"				# The server's hostname or IP address
PORT = 42069 					# The port used by the server
serverAddrPort = (HOST, PORT)	# Convinience tuple

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

	# client needs to send first communication due to the nature of UDP protocol
	s.sendto(b"Connection init, can you hear me?", serverAddrPort)

	# Getting data from the server
	server_data = s.recvfrom(1024)
	s.sendto(b"I can hear you too!", serverAddrPort)
	
print(f"Received: {server_data[0].decode()}")