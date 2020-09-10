import socket
import select

HEADER = 10
PORT = 1234
IP = '127.0.0.1'
ADDR = (IP, PORT)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)

server_socket.bind(ADDR)
server_socket.listen()

sockets_list = [server_socket]

clients = []

print('listing....')



def inconing(client_socket):

    try:
        message_header = client_socket.recv(HEADER)

        if not len(message_header):
            return False
        message_lenth = int(message_header.decode('utf-8').strip())

        return {'header': message_header, 'data': client_socket.recv(message_lenth)}

    except:
        return False

while True:

    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_sockets in read_sockets:

        if notified_sockets == server_socket:
            client_socket, client_address = server_socket.accept()

            user = inconing(client_socket)

            if user is False:
                continue

            sockets_list.append(client_socket)

            clients[client_socket] = user

            print('Accepted new connection from {}:{}, username: {}'.format(*client_address,
                                                                           user['data'].decode('utf-8')))

        else:

            # Receive message
            message = inconing(notified_socket)

            # If False, client disconnected, cleanup
            if message is False:
                print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))

                # Remove from list for socket.socket()
                sockets_list.remove(notified_socket)

                # Remove from our list of users
                del clients[notified_socket]

                continue

            # Get user by notified socket, so we will know who sent the message
            user = clients[notified_socket]

            print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            # Iterate over connected clients and broadcast message
            for client_socket in clients:

                # But don't sent it to sender
                if client_socket != notified_socket:
                    # Send user and message (both with their headers)
                    # We are reusing here message header sent by sender, and saved username header send by user when he connected
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

            # It's not really necessary to have this, but will handle some socket exceptions just in case
        for notified_socket in exception_sockets:
            # Remove from list for socket.socket()
            sockets_list.remove(notified_socket)

            # Remove from our list of users
            del clients[notified_socket]
