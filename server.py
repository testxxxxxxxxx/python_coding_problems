import socket
import sys

host = '127.0.0.1'
port = 8084

def connect()->None:

    try:

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

        s.bind( (host, port) )

        s.listen(5)

        c, addr = s.accept()

        s.close()

        sys.exit()

    except socket.error as err:
        raise Exception(err)
    finally:
        print('Socket has been closed')

if __name__ == '__main__':
    connect()
