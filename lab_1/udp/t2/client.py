# UDP client that generates random numbers
# Author: Srikar

import socket
from random import randint
from json import dumps, loads

# Function to get a list of size N ∈ {25, 100} with elements ∈ {1, 100}

def get_rand_list():
	de_list = []
	n = randint(25, 100)
	for i in range(n):
		de_list.append(randint(1, 100))

	return de_list

HOST = "127.0.0.1"				# The server's hostname or IP address
PORT = 42069 					# The port used by the server
serverAddrPort = (HOST, PORT)	# Convinience tuple

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
	
	# Generate a random array AKA list, python things
	arr = get_rand_list()

	# Send the random array
	s.sendto(bytes(dumps(arr), 'utf-8'), serverAddrPort)

	update_list = s.recvfrom(2048)	# Safe hopefully, need to check limit

	update_list = update_list[0].decode()
	update_list = loads(update_list)

	print(f"\nUpdated list: {update_list['arr']}")
	print("\n")
	print(f"Duplicate elements: {update_list['del']}")