import socket
SERVER_PORT=5000
SERVER_IP='localhost'
BUFFER_SIZE=1024*4

if __name__ == '__main__':
    print("Client begin:")
    with socket.socket() as socket:
        socket.connect((SERVER_IP,SERVER_PORT))
        while (True):
            cdata = input("Please inser your message:")
            if (cdata == "Bye"):
                print("Client is dead")
                break
            socket.sendall(cdata.encode())
