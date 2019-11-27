import socket
from appJar import gui
from threading import Thread
import time

dict_of_users = {}
list_of_users= []

def listen_bind(HOST, PORT):
    mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySock.bind((HOST, PORT))
    mySock.listen()
    print('listening...')
    while True:
        conn, adress = mySock.accept()
        print(conn,adress)
        recive_thread = Thread(target=recive_from_user, args=(conn,))
        recive_thread.start()

    return recive_thread

def send_all(data):
    for key in dict_of_users:
        key.sendall(data)


def send_private(namn,connection,msg_from,message):
    medelande= bytes((f"(pm){msg_from}:{message}"),'utf-8')
    connection.sendall(medelande)
    
def close_klient(data,conn):
    data= bytes(data,'utf-8')
    conn.sendall(data)
    

def recive_from_user(conn): 
    while True:
        data = conn.recv(256).decode('utf-8')
        if not data:
            break
        data = format(data)
        
        if data[0] =="#":
            namn = data.strip("#")
            namn= namn.strip("!")
            dict_of_users[conn]=namn 
            for key in dict_of_users:
                for x in dict_of_users:
                    update_name = bytes((f"!{dict_of_users[x]}"),'utf-8')
                    key.sendall(update_name)
                    time.sleep(0.1)

        if "@" in data:
            info=data.split("@")
            namn=info[0]
            msg_from=info[1]
            message= info[2]
            for connection, name in dict_of_users.items():
                if name == namn:
                    send_private(namn, connection, msg_from, message)

        if data[0] =="%":
            returnvalue = data.encode('utf-8')
            send_all(returnvalue)
        
        if "&&close" in data:
            del dict_of_users[conn]
            close_klient("&&close",conn)
            
            


def main():
    HOST_name = socket.gethostname()
    HOST_ip = socket.gethostbyname(HOST_name)
    PORT = 65432
    print("Hostname :  ", HOST_name)
    print("IP : ", HOST_ip)

    listen_bind(HOST_ip, PORT)
    


if __name__ == "__main__":
    main()
