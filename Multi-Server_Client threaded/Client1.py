# Import socket module
import socket


###########################################################
host = '127.0.0.1'  # local host IP '127.0.0.1'
port = 12345  # Define the port on which you want to connect
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
###########################################################


def main():
    s.connect((host, port))   # connect to server on local computer
    message = "Eyal" # message you send to server
    while True:
        s.send(message.encode()) # message sent to server
        data = s.recv(1024) # messaga received from server
        # print the received message
        # here it would be a reverse of sent message
        print('Received from the server :', str(data.decode()))
        # ask the client whether he wants to continue
        ans = input('\nDo you want to continue(y/n) :')
        if ans == 'y':
            continue
        else:
            break
    # close the connection
    s.close()


if __name__ == '__main__':
    main()
