# UDP client that generates blocks of data along with row and column parity
# Author: Srikar

import socket
from random import randint

# Simple function to flip a bit
def flipBit(bit):
	bit += 1
	bit %= 2
	return bit

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


N = 5

matrix = getRandomMatrix(N - 1)
getParity(matrix, N)

for i in range(N):
	print(matrix[i])

# Ideally one should be using __name__ == "__main__", but ehh lite