# UDP client that generates blocks of data along with row and column parity
# Author: Srikar

import socket
from random import randint
from json import dumps

# Simple function to flip a bit
def flipBit(bit):
	bit += 1
	bit %= 2
	return bit


# Function to flip a random bit in the matrix
def flipRandomMatrixBit(matrix, N):
	randX = randint(0, N - 1)
	randY = randint(0, N - 1)
	matrix[randX][randY] = flipBit(matrix[randX][randY])
	print(f"Flipped bit at ({randX}, {randY})")

# Function to get a random matrix having 0s and 1s of size N
def getRandomMatrix(N):
	matrix = []

	for i in range(N):
		matrix.append([])
		for j in range(N):
			matrix[i].append(randint(0, 1))

	return matrix

# Function to initialize parity
def getParity(matrix, N):
	
	matrix.append([])
	
	# Initialzie column parities with 0
	for i in range(N):
		matrix[N - 1].append(0)

	for i in range(N):
		
		parityJ = 0

		for j in range(N - 1):
			if(matrix[i][j]):
				parityJ = flipBit(parityJ)

				matrix[N - 1][j] = flipBit(matrix[N - 1][j])
		
		# For last row check
		if(i != N - 1):
			matrix[i].append(parityJ)
		
		else:
			matrix[i][N - 1] = parityJ

# Function to send data to local server using UDP protocol
def sendMatrix(matrix, N):
	HOST = "127.0.0.1"				# The server's hostname or IP address
	PORT = 42069 					# The port used by the server
	serverAddrPort = (HOST, PORT)	# Convinience tuple

	with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

		# Send the random array
		s.sendto(bytes(dumps({N: matrix}), 'utf-8'), serverAddrPort)

if __name__ == "__main__":
	
	N = 5

	# Generating a random matrix of size N - 1
	matrix = getRandomMatrix(N - 1)

	# Assigning parity for the same
	getParity(matrix, N)

	# Randomly try to introduce an error
	if(randint(0, 1)):
		flipRandomMatrixBit(matrix, N)

	print(dumps({N: matrix}))
	
	# Sending data to the server
	sendMatrix(matrix, N)