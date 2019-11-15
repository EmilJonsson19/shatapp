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
        Thread(target=recive_from_user, args=(conn,)).start()
    return


def send_all():
    pass


def send_private():
    pass


def recive_from_user():
    pass


def main():
    HOST_name = socket.gethostname()
    HOST_ip = socket.gethostbyname(HOST_name)
    PORT = 65432
    print("Hostname :  ", HOST_name)
    print("IP : ", HOST_ip)

    listen_bind(HOST_ip, PORT)


if __name__ == "__main__":
    main()
