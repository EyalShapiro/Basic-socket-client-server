#משיג כתובת IP של אתר 


import socket


def main():
    remote_host = 'www.geekscoders.com'

    try:
        print("IP Address Of " + remote_host + " is " +
              socket.gethostbyname(remote_host))

    except socket.error as e:
        print("Error ", e)


if __name__ == "__main__":
    main()
