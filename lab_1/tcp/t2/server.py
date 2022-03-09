# TCP server to remove and report duplicate elements
# Author: Srikar

import socket
from json import loads, dumps

# Function to delete and return duplicates 
def delete_dups(rand_arr):
	update_list = {}
	update_list['arr'] = []
	update_list['del'] = []

	for i in rand_arr:
		if i not in update_list['arr']:
			update_list['arr'].append(i)
		
		else:
			update_list['del'].append(i)

	return update_list


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

				# Reciving the list
				str_list = conn.recv(1024)	# Size won't be bigger than 500 bytes acc to constraints
				rand_arr = loads(str_list.decode())

				# Sending updated json
				send_str = dumps(delete_dups(rand_arr))

				conn.sendall(bytes(send_str, 'utf-8'))

		except KeyboardInterrupt:
			print('Shutting down the server...')
			break

		# We should ideally never hit this, but nobody can predict the future ¯\_(ツ)_/¯
		except Exception as e:
			print(f"Something bad happened: {e}")