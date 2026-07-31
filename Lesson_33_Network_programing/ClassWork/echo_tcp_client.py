import socket

def echo_client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = 'localhost'
    port = 8888

    try:
        client_socket.connect((host, port))
        print(f'Підключено до сервера {host}:{port}')

        while True: