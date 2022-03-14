# UDP server to recieve data and correct errors in it
# Author: Srikar

import socket
from json import loads

from client import flipBit

# Function to find bit error using parity bits
def getFaults(matrix, N):
	faultX = -1
	faultY = -1

	for i in range(N):
		
		parityX = 0
		
		for j in range(N - 1):
			if(matrix[i][j]):
				parityX = flipBit(parityX)

		# Check if we found the error row
		if (parityX != matrix[i][N - 1]):
			faultX = i
			break

	for j in range(N):
		
		parityY = 0
		
		for i in range(N - 1):
			if(matrix[i][j]):
				parityY = flipBit(parityY)

		# Check if we found the error row
		if (parityY != matrix[N - 1][j]):
			faultY = j
			break

	if(faultX * faultY >= 0):
		return (faultX, faultY)

# Function to listen for clients
def getDataFromClient():
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
				str_data = s.recvfrom(2048)
				
				client_addr = str_data[1]
				str_data = str_data[0]
				print(f"\nConnected to {client_addr}")

				data_json = loads(str_data.decode())

				for i in data_json:
					getFaults(data_json[i], int(i))

			except KeyboardInterrupt:
				print('Shutting down the server...')
				break

			# We should ideally never hit this, but nobody can predict the future ¯\_(ツ)_/¯
			except Exception as e:
				print(f"Something bad happened: {e}")

if __name__ == "__main__":
	getDataFromClient()