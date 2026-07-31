import socket

def udp_server():

    #Створення сокету для UDP піключення
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    HOST = 'localhost'
    PORT = 5001

    #Прописуємо адресу та порт серверу
    udp_socket.bind((HOST, PORT))
    print(f'UDP - сервер запущено на {HOST}:{PORT}')
    print('Очікуємо повідомлення від клієнта.....')


    try:
        while True:
            data, client_addr = udp_socket.recvfrom(1024)

            # Декодуємо повідомлення від кліента
            message = data.decode()
            print(f"Кліент {client_addr} повідомив: {message}")

            #Відповідь кліенту що сервер отримав повідомлення
            response = f'Сервер отримав {message}'
            udp_socket.sendto(response.encode(), client_addr)

    except KeyboardInterrupt:
        print('Сервер зупинено користувачем')
    finally:
        udp_socket.close()

if __name__ == '__main__':
    udp_server()




