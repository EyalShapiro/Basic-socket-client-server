import socket
c=socket.socket()
c.connect(("127.0.0.1",1729))
c.send("eyal".encode())
