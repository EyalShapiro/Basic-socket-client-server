"""
IP משיג כתובת 
 של המחשב מקומי
"""
import socket


def main():
    hostName = socket.gethostname()

    ipaddr = socket.gethostbyname(hostName)
    print(" Host Name Is : {} " .format(hostName))
    print(" IP Address Is : {} " .format(ipaddr))


if __name__ == "__main__":
    main()
