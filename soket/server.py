import socket

IP = "127.0.0.1"
PORT = 1729
if __name__ == '__main__':
    s = socket.socket()
    s.bind((IP, PORT))
    s.listen()
    c, address = s.accept()
    msg = c.recv(1021).decode()
    print(msg)
