#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__file__ = "server.py"
__auther__ = "B. Alfanous"
__email__ = "b.alfanous@outlook.com"
__date__ = "28/Mar/2020"

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 9000               # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
print ("Got connection from: ", addr)
c.close()                # Close the connection