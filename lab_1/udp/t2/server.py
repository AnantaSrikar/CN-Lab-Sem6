# UDP server to remove and report duplicate elements
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

HOST = "127.0.0.1"				# The server's hostname or IP address
PORT = 42069 					# The port used by the server
serverAddrPort = (HOST, PORT)	# Convinience tuple

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
	try:
		s.bind(serverAddrPort)	# Claim the port

	except OSError:
		print("Port is busy! You're probably running the server already?")
		exit()

	while True:
		try:
			# Client should initiate a connection in UDP, due to the nature of the connectionless protocol
			str_list = s.recvfrom(1024)		# Size won't be bigger than 500 bytes acc to constraints
			
			client_addr = str_list[1]
			str_list = str_list[0]
			print(f"Connected to {client_addr}")

			rand_arr = loads(str_list.decode())

			# Sending updated json
			send_str = dumps(delete_dups(rand_arr))

			s.sendto(bytes(send_str, 'utf-8'), client_addr)

		except KeyboardInterrupt:
			print('Shutting down the server...')
			break

		# We should ideally never hit this, but nobody can predict the future ¯\_(ツ)_/¯
		except Exception as e:
			print(f"Something bad happened: {e}")