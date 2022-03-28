"""
    Basic FTP client
    Author: Srikar
"""

from ftplib import FTP
 
HOST = "localhost"
PORT = 42069

ftp = FTP()

ftp.connect(HOST, PORT)
ftp.login()
 
data = []
 
ftp.dir(data.append)
 
ftp.quit()
 
for line in data:
    print( "-", line)