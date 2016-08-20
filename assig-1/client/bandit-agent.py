import socket
import time

s = socket.socket(socket.AF_INET)
host = socket.gethostname()
port = 5001

s.connect((host, port))
print s.send(bytes(2))

time.sleep(2)

print s.send(bytes(2))
s.close 

