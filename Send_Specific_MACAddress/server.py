import socket
import time

SERVER_ADDRESS = "localhost"
SERVER_PORT = 10000
 
# create a socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  #socket.SO_BROADCAST
server.settimeout(0.2)
address = (SERVER_ADDRESS,SERVER_PORT)
print(f"server {SERVER_ADDRESS} at port {SERVER_PORT}")
server.bind(("",60550))
message = b"This is AJ Testing Broadcast on the network using Python................"
while True:
    # broadcast
    server.sendto(message, ('255.255.255.255', 60551))
    print("message sent!")
    time.sleep(2)