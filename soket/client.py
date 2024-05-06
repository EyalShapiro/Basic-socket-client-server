import socket
IP = "127.0.0.1"
PORT = 1729
if __name__ == '__main__':
    c = socket.socket()
    c.connect((IP, PORT))
    msg = "I am join\nme\tname Eyal "
    c.send(msg.encode())
