import socket

def caesar_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            new_char = chr((ord(char) - start + key) % 26 + start)
            result += new_char
        else:
            result += char
    return result


def create_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    host = 'localhost'
    port = 12345
    server_socket.bind((host, port))

    server_socket.listen(5)

    print(f'Сервер запущено {host}:{port}')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'З"єднання встановлено з {str(client_address)}')

        data = client_socket.recv(1024).decode()
        print(f'Кліент повідомив : {data}')

        message, key = data.split("|")
        key = int(key)

        encrypted = caesar_encrypt(message, key)
        client_socket.send(encrypted.encode())

        client_socket.close()


if __name__ == '__main__':
    create_server()
