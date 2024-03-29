from appJar import gui
import socket
from threading import Thread
import sys

chat_list= []
list_of_users= ["all"]


def send(message, mySocket):

    b = bytes(message, 'utf-8')
    mySocket.sendall(b)



def recieve(mySocket):
    while True:
        data = mySocket.recv(256).decode('utf-8')
        if not data:
            break
        data = format(data)

        if data[0] =="!":
            info= data.strip("!")
            if info not in list_of_users:
                list_of_users.append(info)
                message= (f"{info} has connected to server.")
                chat_list.append(message)
                app.updateListBox("chat",chat_list)
                list_of_users_without_duplicates = check_if_duplicates(list_of_users)
                app.changeOptionBox("user",list_of_users_without_duplicates)

        if "(pm)" in data:
            private_message = data.strip("#")
            chat_list.append(private_message)
            app.updateListBox("chat",chat_list)
        
        
        if data[0]== "%":
            data = data.replace("%","")
            chat_list.append(data)
            app.updateListBox("chat",chat_list)

        if "&&close" in data:
            print("threds stopping")
        
            break
        


def check_if_duplicates(listan): #check if listvalues got duplicates by set
    new_set= set(listan)
    new_list=list(new_set)
    return new_list

def btncallback(btn):    #buttoncallbackfunkition

    if btn == "connect":
        alias = app.getEntry("namn")
        alias= (f"#{alias}")
        send(alias,mySocket)
        
    if btn == "quit":
        send("&&close", mySocket)
        app.stop()
        
    if btn == "send":
        message = app.getEntry("write")         
        current_option = app.getOptionBox("user")
        if current_option !="all":
            alias= app.getEntry("namn")
            header= (f"{current_option}@{alias}@{message}")
            send(header,mySocket)
            app.clearEntry("write")
        else:
            alias = app.getEntry("namn")
            header=(f"%{alias}: {message}")
            send(header, mySocket)
            app.clearEntry("write")
            
        

#skapar GUI
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


def main():
    HOST_name = socket.gethostname()
    HOST_ip = socket.gethostbyname(HOST_name)
    PORT = 65432
    global mySocket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
        mySocket.connect((HOST_ip, PORT))
        print("connected to server and thread for listening established")
        
        listen_thread = Thread(target=recieve, args=(mySocket,))
        listen_thread.start()
        app.go()
        listen_thread.join()
    
 



if __name__ == "__main__":
    main()