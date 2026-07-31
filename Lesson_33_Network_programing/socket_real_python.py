import socket

HOST = '127.0.0.1'
PORT = 63_333

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print('Сервер в режимі очікування кліента.....')

    # Сервер очікує на підключення від клієнта
    conn, addr = server_socket.accept()

    with conn:
        print(f'З`єднано з {addr}, {conn}')

        while True:
            data = conn.recv(1024)
            print(data)
            if not data:
                break
            conn.sendall(data)
