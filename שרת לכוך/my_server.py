import socket
import time
import random

__author__ = " Eyal_Shapiro "
"""
זהו חלק השרת של השקע. הפרוטוקול מציין
    שהוא מקבל את ההודעה הראשונה כ'לחיצת יד ', אליה היא
    מגיב עם סוג השירותים שהוא מספק: הוא מחפש 4
    בעקבות בקשת מכתב:
        Time  ,Name , Rand ,Exit

"""
IP = '0.0.0.0'
PORT = 1729
TIME_PRE = '0'
START_HOUR = -13
END_SEC = -5
MESSAGE_SIZE = 4
RAND_LOW = 1
RAND_HIGH = 10


def format_response(response):
    """
    4 הבתים הראשונים של התגובה הם אורכם. כך שהלקוח
        יודע כמה בתים נותרו לבקשה על ידי recv 4
        בתים ראשונים .
    """
    server_socket = socket.socket()
    server_socket.bind((IP, PORT))
    server_socket.listen()
    (client_socket, client_address) = server_socket.accept()
    print("Client connected")
    print(time.gmtime())
    data = client_socket.recv(1024).decode()
    print("Client sent: " + data)
    reply = "Hello " , data


def inital_listen():
    """
     הפעל את השרת והתחל להאזין להודעות מלקוח
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(1)
    return server


def serve_requests(data, client, server):
    """
    הגשת בקשות על ידי הלקוח, כל עוד הם מגיעים (לולאה)
    """
    while True:
        if data == 'Time':
            response = 'Time is: ', time.gmtime()

        if data == 'Rand':
            response = ' Rand  is: ', str(random.randint(1, 11))

        if data == 'Name':
            response = 'My name is: Eyal'
        elif data == 'Exit':
            break
        else:
            response = 'Bad data, only: TIME, RAND, NAME or EXIT are allowed'
        format_response(response)
        client.send()
        data = client.recv(MESSAGE_SIZE)
    client.close()


def check_client(server):
    client, (ip, port) = server.accept()

    first_response = 'Your options are: TIME, RAND(1-10), NAME , EXIT'
    client.send(first_response.encode())
    '''
   הלקוח אחראי על שליחת 4 בתים בלבד. נוכל לתת לו 
    לשלוח יותר ולהצביע בחזרה על נתונים לא חוקיים (ראה נתונים רעים ... הודעה) 
    '''
    data = client.recv(MESSAGE_SIZE).decode()
    return client, data


def main():
    """
 מקבל את ההודעה הראשונה כלחיצת יד, ואז לולאות
    עד לבקשת Exit, עבור כל בקשה מכינה
    ושולחת את התגובה הנכונה, כולל הערה על
    קלט לא חוקי .
    """
    server = inital_listen()
    while True:
        client, data = check_client(server)
        try:
            serve_requests(data, client, server)
        except:
            client.close()


if __name__ == '__main__':
    main()
