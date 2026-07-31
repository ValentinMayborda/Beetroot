import socket


def create_server():
    # AF_INET - ipv4 (192.168.1.1)
    # SOCK_STREAM - TCP з'єднання
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Для уникнення помилки "Adres already in use"
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    host = 'localhost'
    port = 12345
    server_socket.bind((host, port))

    server_socket.listen(5)

    print(f'Сервер запущено {host}:{port}')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'З"єднання встановлено з {str(client_address)} connected.')

        data = client_socket.recv(1024).decode()
        print(f'Received {data}')

        response = f'Сервер отримав {data}'
        client_socket.send(response.encode())

        client_socket.close()

if __name__ == '__main__':
    create_server()
