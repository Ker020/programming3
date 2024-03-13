import threading
import socket

PORT = 6060
FORMAT = "utf-8"
HEADER = 64
SERVER = "192.168.126.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_message(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def receive_message():
    while True:
        try:
            msg_length = client.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = client.recv(msg_length).decode(FORMAT)
                if msg == "DES":
                    print("Server has terminated the connection.")
                    break
                print(f"Received message from server: {msg}")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

# Start a separate thread to receive messages from the server
receive_thread = threading.Thread(target=receive_message, daemon=True)
receive_thread.start()

while True:
    message = input("Enter a message: ")
    if message.strip() == "":
        continue
    send_message(message)
    if message == "DES":
        break

# Close the client socket when done
client.close()
