import socket
import select
import random

HEADER_LENGTH = 10
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
IP = ''
PORT = 1234

server_ip = socket.gethostbyname(IP)

server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket]

clients = {}

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)

print(f'Listening for connections on {IP}:{PORT}...')


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False

        message_length = int(message_header.decode('utf-8').strip())
        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:
        return False


while True:

    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:

        num1 = random.choice(lista)
        lista.remove(num1)

        num2 = random.choice(lista)
        lista.remove(num2)

        num3 = random.choice(lista)
        lista.remove(num3)

        num4 = random.choice(lista)
        lista.remove(num4)

        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        m = len(lista)
        print(m)

        num5 = random.choice(lista)
        num = f'{num1} {num2} {num3} {num4} {num5}'
        #num = f'{num}'
        print(num)

        numf = num.encode("utf-8")
        num_header = f"{len(numf):<{HEADER_LENGTH}}".encode('utf-8')
        #client_socket.send(num_header + num)

        master = f"Italk"

        master = master.encode("utf-8")
        master_header = f"{len(master):<{HEADER_LENGTH}}".encode('utf-8')

        if notified_socket == server_socket:

            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)

            if user is False:
                continue

            sockets_list.append(client_socket)

            clients[client_socket] = user

            print('Accepted new connection from {}:{}, username: {}'.format(*client_address,
                                                                            user['data'].decode('utf-8')))
            #client_socket.send(user)


        else:

            message = receive_message(notified_socket)

            if message is False:
                print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))

                sockets_list.remove(notified_socket)

                del clients[notified_socket]

                continue

            user = clients[notified_socket]

            print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            for client_socket in clients:

                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

                client_socket.send(master_header + master + num_header + numf)

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)

        del clients[notified_socket]
