#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__file__ = "server.py"
__auther__ = "B. Alfanous"
__email__ = "b.alfanous@outlook.com"
__date__ = "28/Mar/2020"

import socket 

# Reserve a port for your service.
port = 9000
# Get local machine name
host = socket.gethostname()    

# Create a socket object that uses IPv4 and TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
print("Socket created.\n")       
# Bind the socket to host and IP
s.bind((host, port)) 
print(f'Host: {host} Port: {port} are binded.\n')        
# Now wait for client connection.
s.listen(1)
print("Server is listening...\n") 

# Establish connection with client.                 
clientconn, addr = s.accept()     
print ("Connection established to: ", addr)

print("\n**********************************************\n")  

#fileName = input("Enter file name: ")
#clientconn.send(bytes(fileName, "utf-8"))
#print(f'Sending file: {fileName} \n')

f = open('txt.txt', 'rb')

for line in f:
    clientconn.send(line)


f.close()
print("\n**********************************************\n")  

# Close the connection
clientconn.close()
print("Socket Closed.\n")              