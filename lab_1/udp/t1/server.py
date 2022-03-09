# Basic UDP server
# Author: Srikar

import socket

HOST = "127.0.0.1"	# Standard loopback interface address (localhost)
PORT = 42069		# Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
	try:
		s.bind((HOST, PORT))	# Claim the port

	except OSError:
		print("Port is busy! You're probably running the server already?")
		exit()
	
	while True:
		try:
			# Client should initiate a connection in UDP, due to the nature of the connectionless protocol
			data = s.recvfrom(1024)		# Get data from client. data[0] is data and data[1] will be source

			client_addr = data[1]

			print(f"Got message: {data[0].decode()} from {data[1]}")
			
			s.sendto(b"I can hear you!", client_addr)

			data = s.recvfrom(1024)
			print(f"Got message: {data[0].decode()} from {data[1]}")
		
		except KeyboardInterrupt:
			print('Shutting down the server...')
			break

		# We should ideally never hit this, but nobody can predict the future ¯\_(ツ)_/¯
		except Exception as e:
			print(f"Something bad happened: {e}")