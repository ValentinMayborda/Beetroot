import socket

def create_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect(('localhost', 63333))

    message = "Привіт сервер!"
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print(f'Відповідь сервера: {response}')

    client_socket.close()

if __name__ == '__main__':
    create_client()