# UDP server to recieve data and correct errors in it
# Author: Srikar

import socket
from json import loads

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

				print(data_json)

			except KeyboardInterrupt:
				print('Shutting down the server...')
				break

			# We should ideally never hit this, but nobody can predict the future ¯\_(ツ)_/¯
			except Exception as e:
				print(f"Something bad happened: {e}")

if __name__ == "__main__":
	getDataFromClient()