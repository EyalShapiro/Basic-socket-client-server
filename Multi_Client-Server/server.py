import socket
import select
SERVER_IP = '127.0.0.1'
SERVER_PORT = 1729
MAX_MESSAGE_LENGTH = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SERVER_IP, SERVER_PORT))
s.listen()
clients = []
messages = []
while True:
    rlist, wlist, xlist = select.select([s] + clients, clients, [])
    # rlist = לקוחות שהמידע נלקח מהם
    # wlist = לקוחות שכתוב עליהם מידע
    # xlist = לקוחות שהתנתקו
    for client in rlist:
        if client is s:
            print('new client joined')
            c, address = client.accept()
            clients.append(c)
        else:
            message = client.recv(MAX_MESSAGE_LENGTH).decode()
            if message == "":
                print('connection closed')
                clients.remove(client)
                client.close()
            else:
                print(message)
                # messages.append((client, 'from server'))
                clients_to_send = []
                for c in clients:
                    if not c is client:
                        clients_to_send.append(c)
                messages.append((clients_to_send, message))
    for message in messages:
        """
        client, msg = message
        if client in wlist:
            client.send(msg.encode())
            messages.remove(message)
        """
        clients_to_send, msg = message
        for client in clients_to_send:
            if client in wlist:
                client.send(msg.encode())
        messages.remove(message)
s.close()
