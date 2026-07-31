import socket
import select


def echo_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    host = 'localhost'
    port = 8888

    server_socket.bind((host, port))

    server_socket.listen(5)

    print(f'Ехо-сервер запущено на: {host}:{port}')
    socket_list = [server_socket]

    clients = {}
    try:
        while True:
            read_sockets, _, exception_sockets = select.select(socket_list, [], [], 0)
            for notified_socket in read_sockets:
                if notified_socket == server_socket:
                    client_socket, client_address = server_socket.accept()
                    print(f'Нове підключення від {client_address}')
                    socket_list.append(client_socket)
                    clients[client_socket] = {
                        'address': client_address,
                        'message_count': 0,
                    }
                else:
                    try:
                        data = notified_socket.recv(1024)
                        if data:
                            message = data.decode()

                            clients[notified_socket]['message_count'] += 1
                            count = clients[notified_socket]['message_count']
                            print(f'Отримано від {clients[notified_socket]["address"]}: {message}')
                            response = f"Повідомлення #{count}: {message} має {len(message)} символів."
                            notified_socket.send(response.encode())
                        else:
                            print(f'Клієнт {clients[notified_socket]["address"]} відключився')
                            socket_list.remove(notified_socket)
                            del clients[notified_socket]
                            notified_socket.close()
                    except Exception as e:
                        print(f'Помилка при отриманні даних: {e}')
                        socket_list.remove(notified_socket)
                        del clients[notified_socket]
                        notified_socket.close()


            for notified_socket in exception_sockets:
                print(f'Помилка на сокеті {clients.get(notified_socket, {}).get("address", "Unknown")}')
                socket_list.remove(notified_socket)
                if notified_socket in clients:
                    del clients[notified_socket]

                notified_socket.close()
    except KeyboardInterrupt:
        print('\nСервер зупинено користувачем')

    finally:
        server_socket.close()

        for client_socket in socket_list:
            if client_socket != server_socket:
                client_socket.close()
        print('Всі сокети закрито')

if __name__ == '__main__':
     echo_server()