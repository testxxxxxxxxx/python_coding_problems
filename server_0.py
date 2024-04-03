import socket
import sys

host: str = '127.0.0.1'
port: int = 8085

def connect() -> None:

    try:

        s: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

        s.setsockopt(socket.SOL_SOCKET ,socket.SO_REUSEADDR | socket.SO_REUSEPORT, 1)

        s.bind((host, port))

        s.listen(5)

        (c, addr) = s.accept()

        s.close()

    except socket.error as err:
        raise Exception(err)
    finally:
        print(f"Connection has been closed!")

if __name__ == '__main__':
    connect()