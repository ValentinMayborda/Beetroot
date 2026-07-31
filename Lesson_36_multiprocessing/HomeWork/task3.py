import socket
from multiprocessing import Process


def client_connection(connection):
    try:
        while True:
            data = connection.recv(1024)

            if not data:
                break
            print(f'Отримано: {data.decode()}')
            connection.sendall(data)

    except Exception as e:
        print(f'Помилка {e}')
    finally:
        print('Клієнт відключився')
        connection.close()


if __name__ == '__main__':

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(('localhost', 8080))
    server_socket.listen()
    print("Сервер в очікуванні клієнтів.....")

    try:
        while True:
            connection, client_address = server_socket.accept()
            print(f'Під`єднався: {client_address}')

            process = Process(target=client_connection, args=(connection,))

            process.start()
            connection.close()

    except KeyboardInterrupt:
        print('Сервер зупинено')
    finally:
        server_socket.close()
