import socket

s = socket.socket()
host = input(str("Host name: "))
port = 9000
s.connect((host, port))
print("Connected...")

fileName = "demo.mp3"
with open(fileName, 'rb') as file:
	fileData = file.read(1024)
	while fileData:
		s.send(fileData)
		fileData = file.read(1024)


#file = open(fileName, 'rb')
#fileData = file.read(1024)
#s.send(fileData)

import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()  #Ip address that the TCPServer  is there
port = 50000                     # Reserve a port for your service every new transfer wants a new port or you must wait.

s.connect((host, port))
s.send("Hello server!")

with open('demo1.mp3', 'wb') as f:
    print ('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')


import socket                   # Import socket module

port = 50000                    # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket()             # Create a socket object
host = socket.gethostname()   # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print ('Server listening....')


while True:
    conn, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='demo.mp3' #In the same folder or path is this file running must the file you want to tranfser to be
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       #print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()


############################################
