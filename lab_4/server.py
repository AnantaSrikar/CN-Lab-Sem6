"""
	Basic FTP server
	Author: Srikar
"""

from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer

address = ("127.0.0.1", 42069)

if __name__ == "__main__":
		
	authorizer = DummyAuthorizer()
	authorizer.add_anonymous("./server_root", perm='elradfmwMT')

	handler = FTPHandler
	handler.authorizer = authorizer

	server = servers.FTPServer(address, handler)
	server.serve_forever()