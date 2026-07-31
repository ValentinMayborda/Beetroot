import socket

def create_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect(('localhost', 8080))


    message = "Hello Server!"
    client_key = '5'
    client_socket.send(f'{message}|{client_key}'.encode())

    response = client_socket.recv(1024).decode()
    print(f'Відповідь сервера: {response}')

    client_socket.close()

if __name__ == '__main__':
    create_client()