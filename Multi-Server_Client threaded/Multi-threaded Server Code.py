# import socket programming library
import socket

# import thread module
from _thread import *
import threading

###########################################################
print_lock = threading.Lock()
host_ip = '127.0.0.1'  # local host IP '127.0.0.1'
# reverse a port on your computer
# in our case it is 12345 but it
# can be anything
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host_ip, port))

###########################################################


def threaded(c):  # thread function
    while True:
        data = c.recv(1024)  # data received from client
        if not data:
            print('Bye')
            # lock released on exit
            print_lock.release()
            break
        data = data[::-1]  # reverse the given string from client
        c.send(data)  # send back reversed string to client
    c.close()  # connection closed


def Main():
    print("socket binded to port", port)
    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '__main__':
    Main()
