#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__file__ = "client.py"
__auther__ = "B. Alfanous"
__email__ = "b.alfanous@outlook.com"
__date__ = "28/Oct/2019"

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 9000                # Reserve a port for your service.
s.connect((host, port))
s.close()                     # Close the socket when done