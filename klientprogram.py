from appJar import gui
import socket
from threading import Thread


def showGui():
    app = gui("ShatApp", "500x500")
    app.setBg("lightslategrey")
    app.addLabel(
        "welcomemsg", "Write a aliasname below and press connect to start using ShatApp!")

    app.startFrame("first")
    app.setBg("lightslategrey")
    app.addEntry("namn", row=0)
    app.addButtons(["connect", "show users", "quit"], [
                   btncallback, btncallback, btncallback])
    app.stopFrame()
    app.startFrame("second")
    app.setBg("lightslategrey")
    app.setSticky("wsn")
    app.addVerticalSeparator(colour="black", row=0, column=0)
    app.setSticky("ew")
    app.addListBox("chat", row=0, column=1)
    app.setSticky("esn")
    app.addVerticalSeparator(colour="black", row=0, column=2, colspan=4)
    app.stopFrame()
    app.startFrame("third")
    app.setBg("lightslategrey")
    app.addEntry("write")
    app.addButtons(["send", "ABC", "abc"], [
                   btncallback, btncallback, btncallback])
    app.stopFrame()
    app.go()


def btncallback(btn):
    if btn == "connect":
        pass
    if btn == "quit":
        pass


def connect_to_server():
    pass


def recieve():
    pass


def main():
    pass


if __name__ == "__main__":
    main()

showGui()
