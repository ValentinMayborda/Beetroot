import socket

def udp_server():
    # SOCK_DGRAM - UDP протокол
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_adress = ('localhost', 12345)
    server_socket.bind(server_adress)

    print(f'UDP - сервер запущено на {server_adress[0]}:{server_adress[1]}')
    print('Очікуємо повідомлення від клієнта.....')

    try:
        while True:
            data, client_address = server_socket.recvfrom(1024)
            message = data.decode()
            print(f'Отримано від {client_address}: {message}')
            response = f'Сервер отримав {message}'

            server_socket.sendto(response.encode(), client_address)
    except KeyboardInterrupt:
        print('\nСервер зупинено користувачем')
    finally:
        server_socket.close()
        print('Сокет закрито')

if __name__ == '__main__':
    udp_server()
