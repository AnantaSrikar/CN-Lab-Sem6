"""
	Basic FTP client
	Author: Srikar
"""

from ftplib import FTP
from os import system, remove
from os.path import basename

# Fixed server details
HOST = "localhost"
PORT = 42069

# Funtion to print basic exception that is unhandlable
def printRandException(e):
	print(f"Something bad happened: {e}")

# Function to list all files and directories on the server
def ftpLS(ftp):
	print("Files on the server: ")
	
	data = []

	ftp.dir(data.append)

	for line in data:
		print("-", line)

# Function to upload files to server
def uploadToServer(ftp, local_file_path):
	try:
		with open(local_file_path, "rb") as inFPtr:
			ftp.storbinary(f"STOR {basename(local_file_path)}", inFPtr)
		print(f"Uploaded {basename(local_file_path)} successfully!")
	except Exception as e:
		printRandException(e)


# Function to download file from server
def downloadFromServer(ftp, remote_file_path):
	try:
		with open(basename(remote_file_path), "wb") as outFPtr:
			ftp.retrbinary(f"RETR {remote_file_path}", outFPtr.write)

	except Exception as e:
		printRandException(e)
		remove(basename(remote_file_path))

if __name__ == "__main__":

	ftp = FTP()

	try:
		ftp.connect(HOST, PORT)	# To connect to the server
		ftp.login()	# Anonymous login

	except ConnectionRefusedError:
		print("Unable to connect to server, is it running?")
		exit()
	
	except Exception as e:
		printRandException(e)
		exit()

	while(True):
		choice = input("\n1. See all files on server\n2. Upload file to server\n3. Download a file from server\nAnd anything else to exit!\n\nEnter choice: ")

		try:
			choice = int(choice)
		except ValueError:
			pass

		system('clear')

		if choice == 1:	# To list all files and dirs on server
			ftpLS(ftp)
		
		elif choice == 2:	# To upload a file to server
			# Probably have file autocompletion here. Will implement if I get enough sleep this week
			local_file_path = input("Enter absolute file path: ")
			uploadToServer(ftp, local_file_path)

		elif choice == 3:	# To download a file to server
			# File path autocompletion possible here as well. But I need sleep
			remote_file_path = input("Enter absolute file path: ")
			downloadFromServer(ftp, remote_file_path)

		else:
			print("Exitting...")
			break

	ftp.quit()