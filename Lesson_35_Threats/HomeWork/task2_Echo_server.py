import socket
import threading

def keep_client_connection(connection):
    while True:
        data = connection.recv(1024)

        if not data:
            break
        print(f'Отримано: {data.decode()}')
        connection.sendall(data)
    connection.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 8080))
server_socket.listen()
print("Сервер в очікуванні клієнтів.....")

while True:
    connection, client_address = server_socket.accept()
    print(f'Під`єднався: {client_address}')

    thread = threading.Thread(target=keep_client_connection, args=(connection,))

    thread.start()