import socket

HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    client_socket.sendall(b"Hello serv!")

    data = client_socket.recv(1024)

    print(f'Отримано відповідь від сервера: {data!r}')
    print(f'Отримано відповідь від сервера:', repr(data))