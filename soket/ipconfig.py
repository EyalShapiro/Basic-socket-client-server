import socket


def Extract_Ip():
    '''
    הפעולה בודקת את כתובת האינטרנט של המחשב
    windows ב
    '''
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP


def main():

    print("your ip :"+Extract_Ip())


if __name__ == '__main__':
    main()