from zlib import compress, decompress
import file_ext
import socket
import os

class Server_Client():
    def __init__(self):
        pass
    #=========================================SERVER==============================================#
    
    def file_server(self, HOST, PORT, file_to_sent):
        port = PORT
        s = socket.socket()
        host = HOST
        s.bind((host, port))
        s.listen(5)

        print('Server listening....')


        while True:
            conn, addr = s.accept()
            print('Got connection from', addr)
            data = conn.recv(1024)
            print('Server received', repr(data))

            filename=file_to_sent
            f = open(filename,'rb')
            l = f.read(1024)
            while (l):
                conn.send(l)
                print('Sent ',repr(l))
                l = f.read(1024)
            f.close()

            print('Done sending')
            quit()
            conn.close()
            
    def file_client(self, HOST, PORT, file_to_save):
        s = socket.socket()
        host = HOST
        port = PORT

        s.connect((host, port))
        s.send(b"Hello server!")

        with open(file_to_save, 'wb') as f:
            print('file opened')
            while True:
                print('receiving data...')
                data = s.recv(1024)
                print('data=%s', (data))
                if not data:
                    break

                f.write(data)

        f.close()
        print('Successfully get the file')
        s.close()
        print('connection closed')
    #=======================================END-SERVER============================================#

from sys import argv

if __name__ == "__main__":
    s = Server_Client()
    if argv[1] == "server":
        s.file_server("localhost", 5000, "GOALS")
    elif argv[1] == "client":
        s.file_client("localhost", 5000, "something.txt")