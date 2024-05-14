import threading
import socket
import time

PORT = 6060
FORMAT = "utf-8" #type of write
D = "DES"
HEADER = 64 #size of message
hostname = socket.gethostname()
SERVER = socket.gethostbyname(hostname) #ip adderss
ADDR = (SERVER,PORT) # to connect use ip and port
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def send ():
    pass



def client (conn, addr):
    print(f"{ADDR} is connected")
    connected = True
    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len) #size of message will come
            msg =conn.recv(msg_len).decode(FORMAT) # recve message and utf-8
            if msg == D:
                connected =False # clase sation after massage = DES
            print(f"{addr} {msg}")
    conn.close()




def start():
    server.listen()
    print(f"the server is listening to {SERVER}")
    while True:
        conn, adrr = server.accept()
        thread = threading.Thread(target=client , args=(conn, adrr))
        thread.start() 

print ("the server is starting")
start()
