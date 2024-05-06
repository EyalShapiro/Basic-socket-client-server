import socket
import random

__author__ = " Eyal_Shapiro "
"""
זהו חלק הלקוח של השקע. הוא יכול לבקש את הדברים הבאים
    שירותים
    Time  ,Name , Rand ,Exit
"""
SERVER = '127.0.0.1'
PORT = 1729
FIRST_MESSAGE_LENGTH = 48
MESSAGE_SIZE = 4


def initial_contact(ip, port):
    """
    שולח את לחיצת היד הראשונה לשרת ובקש את
        השירותים שהוא מספק.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((ip, port))

    except:
        print('Server is not up , yet')
        return 'False', '', ''
    result = client_socket.recv(FIRST_MESSAGE_LENGTH)
    print(result)
    return 'True', result, client_socket


def send_requests(data, client_socket):
    """
 שאל את המשתמש מה היא רוצה, שולח אותו לשרת ומדפיס
        את תשובת השרת על גבי המסך. ואז שאל את המשתמש שוב
    """
    my_socket = socket.socket()
    my_socket.connect((SERVER, PORT))
    requests = input("Enter One of the list (Time  ,Name , Rand ,Exit) : ")
    while requests != "Exit":
        client_socket.send(requests.encode())
        data = my_socket.recv(1024).decode()
        print("The server sent ", data)
        requests = input("Enter One of the list (Time  ,Name , Rand ,Exit) : ")
    client_socket.close()
    pass


def main():
    """
     לבקש מהשרת את סוג השירותים שהוא מספק, ואז לולאה על בקשות.
    """

    server_on, data, socket = initial_contact(SERVER, PORT)
    if server_on:
        send_requests(data, socket)
    #.close()


if __name__ == '__main__':
    main()
