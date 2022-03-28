"""
	Basic FTP client
	Author: Srikar
"""

from ftplib import FTP
from os import system

# Fixed server details
HOST = "localhost"
PORT = 42069

# Function to list all files and directories on the server
def ftpLS(ftp):
	print("Files on the server: ")
	
	data = []

	ftp.dir(data.append)

	for line in data:
		print("-", line)

def uploadToServer(ftp, local_file_path):
	print(f"Upload {local_file_path} to server")

	try:
		with open(local_file_path, "rb") as inFPtr:
			# TODO: Make file name dynamic
			ftp.storbinary("STOR teeest.txt", inFPtr)
		print(f"Uploaded {local_file_path} successfully!")
	except Exception as e:
		print(f"Something bad happened: {e}")

def downloadFromServer(ftp, remote_file_path):
	print(f"Download {remote_file_path} from server")

if __name__ == "__main__":

	ftp = FTP()

	ftp.connect(HOST, PORT)	# To connect to the server
	ftp.login()	# Anonymous login

	while(True):
		choice = input("\n1. See all files on server\n2. Upload file to server\n3. Download a file from server\nAnd anything else to exit!\n\nEnter choice: ")
		choice = int(choice)

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