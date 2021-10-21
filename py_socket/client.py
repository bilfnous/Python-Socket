#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__file__ = "client.py"
__auther__ = "B. Alfanous"
__email__ = "b.alfanous@outlook.com"
__date__ = "28/Oct/2019"

import socket

# Get Server Address      
host = input("Enter server address, enter for current machine: ") or socket.gethostname()
host = int(host)
# Reserve a port for your service.
port = 9000  

# Create a socket object that uses IPv4 and TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
print("Socket created.\n")           
s.connect((host, port))
print(f'Host: {host} Port: {port} are binded.\n')     

print("\n**********************************************\n")  

fileName = s.recv(1024)
fName = fileName.decode("utf-8")
print(f'Receiving file {fName} \n')

f = open(fName, 'ab')
print('receiving data...')

while True:
    data = s.recv(1024)
    if not data:
        break
    # write data to a file
    f.write(data)
f.close()

print("\n**********************************************\n")  
# Close the socket when done
s.close()
print("Socket Closed.\n")                       