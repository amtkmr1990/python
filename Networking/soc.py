import socket
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('msn.com', 80))

s.sendall(b'GET / HTTP/1.1\nHOST: MSN.COM\n\n')
banner = s.recvfrom(1024)

b = banner[0].decode('utf-8')
print(b)
print(re.search('Server:', b))

