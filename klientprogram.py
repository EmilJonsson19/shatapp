from appJar import gui
import socket
from threading import Thread

public_chat_list= []
list_of_users= ["all"]

def connect_to_server():
    HOST_name = socket.gethostname()
    HOST_ip = socket.gethostbyname(HOST_name)
    PORT = 65432
    global mySocket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
        mySocket.connect((HOST_ip, PORT))
        print("connected to server and thread for listening established")
        
        while True:
            listen_thread = Thread(target=recieve, args=(mySocket,))
            listen_thread.start()
            
            
def send(message, mySocket):

    b = bytes(message, 'utf-8')
    mySocket.sendall(b)




def recieve(mySocket):
    while True:
        data = mySocket.recv(1024).decode('utf-8')
        if not data:
            break
        app.updateListBox("chat",public_chat_list)


    

def btncallback(btn):

    if btn == "connect":
        alias = app.getEntry("namn")
        list_of_users.append(alias)
        app.changeOptionBox("user", list_of_users)
        app.thread(connect_to_server)
    if btn == "quit":
        send("close", mySocket)
        mySocket.close()
    if btn == "send":
        message = app.getEntry("write")
        current_option = app.getOptionBox("user")
        if current_option !="all":
            print("it works")
        public_chat_list.append(message)
        send(message, mySocket)
        app.clearEntry("write")
        
        


app = gui("ShatApp", "500x500")
app.setBg("lightslategrey")
app.addLabel(
    "welcomemsg", "Write a aliasname below and press connect to start using ShatApp!")
app.startFrame("first")
app.setBg("lightslategrey")
app.setStretch("both")
app.addEntry("namn", row=0,column=1,colspan=1)
app.stopFrame()
app.startFrame("second")
app.setPadding("10","10")
app.setSticky("ew")
app.addButtons(["connect", "quit"], [btncallback, btncallback],row=1,column=0)
app.addOptionBox("user", list_of_users,row=1,column=1)
app.stopFrame()
app.startFrame("third")
app.setBg("lightslategrey")
app.setSticky("wsn")
app.addVerticalSeparator(colour="black", row=0, column=0)
app.setSticky("ew")
app.addListBox("chat", row=0, column=1)
app.setSticky("esn")
app.addVerticalSeparator(colour="black", row=0, column=2, colspan=4)
app.stopFrame()
app.startFrame("fourth")
app.setBg("lightslategrey")
app.addEntry("write")
app.addButtons(["send", "ABC", "abc"], [
    btncallback, btncallback, btncallback])
app.stopFrame()

app.go()
