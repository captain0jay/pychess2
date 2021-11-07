import socket
HEADER=64
FORMAT='utf-8'
DISCONNECT_MESSAGE='!DISCONNECT'
SERVER="3.134.125.175"
PORT=10329
ADDR=(SERVER,PORT)

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    client.send(message)
    recv_msg=client.recv(HEADER).decode(FORMAT)
    return recv_msg
connected=True
send(" false")
while connected:
    recv_msg=send(input("> "))
    if recv_msg:
        if recv_msg==DISCONNECT_MESSAGE:
            print("you are disconnecting...\n DISCONNECTED")
            connected=False
            break
        print(recv_msg)
        
