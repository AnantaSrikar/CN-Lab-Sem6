# Basic TCP server
# Author: Srikar

import socket

HOST = "127.0.0.1"	# Standard loopback interface address (localhost)
PORT = 42069		# Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	try:
		s.bind((HOST, PORT))
		s.listen()

	except OSError:
		print("Port is busy! You're probably running the server already?")
		exit()

	while True:
		try:
			conn, addr = s.accept()
			with conn:
				print(f"Connected by {addr}")
				conn.sendall(b"Can you hear me?")
				client_data = conn.recv(1024)
				print(f"Recieved from Client: {client_data.decode()}")

		except KeyboardInterrupt:
			print('Shutting down the server...')
			break

		# We should ideally never hit this, but nobody can predict the future ¯\_(ツ)_/¯
		except Exception as e:
			print(f"Something bad happened: {e}")