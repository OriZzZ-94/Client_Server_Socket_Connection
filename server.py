import socket

SERVER_PORT=5001
SERVER_IP='localhost'
BUFFER_SIZE=1024*4
if __name__ == '__main__':
    print("Server begin:")
    with socket.socket() as socket:
        socket.bind((SERVER_IP,SERVER_PORT))
        print("server is binded")
        socket.listen()
        print("server is waiting for a connection...")
        while(True):
            csoc,caddress=socket.accept()
            print("server is connected to"+ str(caddress))
            with csoc:
                while(True):
                    data=csoc.recv(BUFFER_SIZE)
                    if not data:
                        print("Server : client"+str(caddress)+"is disconnected")
                        break
                    else:
                        print("Server: client sent:"+ data.decode())

    print("server is dead")