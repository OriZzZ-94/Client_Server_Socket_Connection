import socket
import threading

SERVER_PORT=5002
SERVER_IP='localhost'
BUFFER_SIZE=1024*4


def thread_function(caddress,csoc):
    print("server is connected to" + str(caddress))
    with csoc:
        while (True):
            data = csoc.recv(BUFFER_SIZE)
            if not data:
                print("Server : client" + str(caddress) + "is disconnected")
                return
            else:
                response = 'HTTP/1.0 200 OK\n\n'+data.decode()
                csoc.sendall(response.encode())
                csoc.close()

if __name__ == '__main__':
    print("Server begin:")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
        socket.bind((SERVER_IP,SERVER_PORT))
        print("server is binded")
        socket.listen()
        print("server is waiting for a connection...")
        while(True):
            csoc,caddress=socket.accept()
            x=threading.Thread(target=thread_function,args=(caddress,csoc))
            x.start()

    print("server is `dead")





