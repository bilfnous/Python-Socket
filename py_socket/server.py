import socket

s = socket.socket()
host = socket.gethostname()
port = 9000
s.bind((host, port))
s.listen(1)
print(host)
conn ,addr = s.accept()

fileName = "rec.mp3"
with open(fileName, 'ab') as file:
	while True:
		file_data = conn.recv(1024)
		if not file_data:
			break
		file.write(file_data)

#file = open(fileName, 'wb')
#file_data = conn.recv(1024)
#file.write(file_data)
#file.close()