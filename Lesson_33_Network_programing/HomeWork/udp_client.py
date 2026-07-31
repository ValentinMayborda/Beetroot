import socket


def udp_client():
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    serv_addres = ('localhost', 5001)

    try:
        while True:
            message = input('Введіть повідомлення для сервера (q - вихід)\n >')

            if message.lower() == 'q':
                break

            udp_client.sendto(message.encode(), serv_addres)

            udp_client.settimeout(5)

            try:
                data, server = udp_client.recvfrom(1024)
                response = data.decode()
                print(f'Відповідь від сервера{serv_addres}: {response}')
            except socket.timeout:
                print('Сервер не відповідає')
    except KeyboardInterrupt:
        print('Клієнт зупинено користувачем')
    finally:
        udp_client.close()
        print("Сокет закрито!")

if __name__ == '__main__':
    udp_client()