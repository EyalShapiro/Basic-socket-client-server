import socket
import select
import msvcrt
import sys

SERVER_IP = '127.0.0.1'
SERVER_PORT = 1729
MAX_MESSAGE_LENGTH = 1024
name = input("enter client name: ")
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((SERVER_IP, SERVER_PORT))
# c.send('from client'.encode())
# message = client_socket.recv(MAX_MESSAGE_LENGTH).decode()
# print(message)
input_from_user = ''
while True:
    rlist, wlist, xlist = select.select([c], [c], [])
    for client in rlist:
        message = client.recv(MAX_MESSAGE_LENGTH).decode()
        if message == '':
            continue  # break
        print(message)
    # do other things in project
    if msvcrt.kbhit():
        keypressed = msvcrt.getch().decode()
        # sys.stdout.write(keypressed) # print(keypressed, end='')
        print(keypressed, end='', flush=True)
        if keypressed == '\r' or keypressed == '\n':
            print(flush=True)  # sys.stdout.write('\n')
            # c.send(input_from_user.encode())
            c.send((name + ': ' + input_from_user).encode())
            input_from_user = ''
        else:
            input_from_user += keypressed
c.close()
