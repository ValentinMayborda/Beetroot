import socket

def udp_client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('localhost', 12345)

    try:
        while True:
            messege = input('Введіть повідомлення для сервера (або вихід для завершення): \n')

            if messege.lower() == 'вихід':
                break

            client_socket.sendto(messege.encode(), server_address)

            client_socket.settimeout(5)
            try:
                data, server = client_socket.recvfrom(1024)
                response = data.decode()
                print(f"Відповідь від сервер: {response}")
            except socket.timeout:
                print(f"Таймаут: сервер не відповідає")
    except KeyboardInterrupt:
        print('Кліент зупинено користувачем')
    finally:
        client_socket.close()
        print('Сокет закрито')

if __name__ == '__main__':
    udp_client()