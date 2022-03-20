# UDP client that sends a string with 2-D parity
# Author: Srikar

import socket
from random import randint
from json import dumps

# No of columns. 8 because char is 8 bits long
N = 8

# Simple function to flip a bit
def flipBit(bit):
	bit += 1
	bit %= 2
	return bit

# Function to flip a random bit in the matrix
def flipRandomMatrixBit(matrix):
	randX = randint(0, len(matrix) - 1)
	randY = randint(0, N - 1)
	matrix[randX][randY] = flipBit(matrix[randX][randY])
	print(f"Flipped bit at ({randX}, {randY})")

# Function to convert string to bits
def getMatrixFromString(input_str):
	
	matrix = []

	# Iterate through all letters
	for i in range(len(input_str)):
		matrix.append([])

		for j in range(7):
			matrix[i].append(0)

		# Filling in reverse to ensure proper placement of bits
		j = 6
		# First, ord gets decimal, then convert that to binary and string for getting individual bits
		# Finally convert to int to make it compatible with previous code
		for de_char in str(bin(ord(input_str[i])))[2:][::-1]:
			matrix[i][j] = (int(de_char))
			j -= 1
	
	return matrix

# Function to initialize parity
def getParity(matrix):

	# Number of rows
	M = len(matrix) + 1

	print(M, N)
	
	matrix.append([])
	
	# Initialzie column parities with 0
	for i in range(N):
		matrix[M - 1].append(0)

	for i in range(M):
		
		parityJ = 0

		for j in range(N - 1):
			
			if(matrix[i][j]):

				parityJ = flipBit(parityJ)

				# Skip flipping column bits on last row
				if(i < M - 1):
					matrix[M - 1][j] = flipBit(matrix[M - 1][j])
		
		# For last row check
		if(i != M - 1):
			matrix[i].append(parityJ)
		
		else:
			matrix[i][N - 1] = parityJ

# Function to send data to local server using UDP protocol
def sendMatrix(matrix):
	HOST = "127.0.0.1"				# The server's hostname or IP address
	PORT = 42069 					# The port used by the server
	serverAddrPort = (HOST, PORT)	# Convinience tuple

	with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

		# Send the random array
		s.sendto(bytes(dumps(matrix), 'utf-8'), serverAddrPort)

if __name__ == "__main__":
	
	input_str = input("Enter string to be sent: ")

	# Generating a random matrix of size N - 1
	matrix = getMatrixFromString(input_str)

	for i in range(len(matrix)):
		print(matrix[i])

	# Assigning parity for the same
	getParity(matrix)

	for i in range(len(matrix)):
		print(matrix[i])

	# Randomly try to introduce an error
	if(randint(0, 1)):
		flipRandomMatrixBit(matrix)

	print("\n")

	for i in range(len(matrix)):
		print(matrix[i])
	
	# Sending data to the server
	sendMatrix(matrix)