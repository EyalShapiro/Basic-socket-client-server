import socket
s = socket.socket()
s.bind(("127.0.0.1", 1729))
s.listen()
c, address = s.accept()
msg = c.recv(1021).decode()
print(msg)
