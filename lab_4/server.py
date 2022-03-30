"""
	Basic FTP server
	Author: Srikar
"""

from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer

from os.path import isdir
from os import makedirs

address = ("127.0.0.1", 42069)

server_root_path = './server_root'

if __name__ == "__main__":

	if not isdir(server_root_path):
		makedirs(server_root_path)
		
	authorizer = DummyAuthorizer()
	authorizer.add_anonymous("./server_root", perm='elradfmwMT')

	handler = FTPHandler
	handler.authorizer = authorizer

	server = servers.FTPServer(address, handler)
	server.serve_forever()