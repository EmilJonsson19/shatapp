import socket
from appJar import gui
from threading import Thread

dict_of_users = {}


def server_gui():
    pass


def listen_bind(HOST, PORT):
    mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    mySock.bind((HOST, PORT))
    mySock.listen()
    print('listening...')
    while True:
        conn, adress = mySock.accept()
        print(conn, adress)
        dict_of_users[conn] = adress
        recive_thread = Thread(target=recive_from_user, args=(conn,))
        recive_thread.start()

    return recive_thread


def send_all(data):
    for key in dict_of_users:
        key.sendall(data)


def send_private():
    pass


def recive_from_user(conn):
    while True:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break
        data = format(data)
        returnvalue = data.encode('utf-8')
        send_all(returnvalue)


def main():
    HOST_name = socket.gethostname()
    HOST_ip = socket.gethostbyname(HOST_name)
    PORT = 65432
    print("Hostname :  ", HOST_name)
    print("IP : ", HOST_ip)

    recive_thread = listen_bind(HOST_ip, PORT)
    print(recive_thread.is_alive())
    recive_thread.join()


if __name__ == "__main__":
    main()
