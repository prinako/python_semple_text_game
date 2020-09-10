import socket
import threading
import sys
import errno

def reciv():

    while True:
        try:
            while True:
                user_header = client_socket.recv(HEADER)

                if not len(user_header):
                    print('cononection closed by the server')
                    sys.exit()

                user_length = int(user_header.decode("utf-8").strip())
                user = client_socket.recv(user_length).decode('utf-8')

                msg_header = client_socket.recv(HEADER)
                msg_length = int(msg_header.decode('utf-8').strip())
                msg = client_socket.recv(msg_length).decode('utf-8')
                #ocket_client.start_listening()

                print(f'\n {user} > {msg}')

        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: {}'.format(str(e)))

            continue

def send():
    message = f"{msg}"
    message = message.encode('utf-8')
    message_header = f"{len(message):<{HEADER}}".encode('utf-8')
    client_socket.send(message_header + message)



HEADER = 10
IP = '127.0.0.1'
PORT = 5555
ADRR = (IP, PORT)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADRR)
#client_socket.listen()


recive_thread = threading.Thread(target=reciv)
recive_thread.start()

USER_NAME = input('username: ')
if USER_NAME:
    username = USER_NAME.encode('utf-8')
    username_header = f'{len(username):<{HEADER}}'.encode('utf-8')
    client_socket.send(username_header + username)

while True:
    msg = input(f'{USER_NAME} > ')
    if msg:
        send()
