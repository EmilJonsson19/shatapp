import unittest



class testCases(unittest.TestCase):

    def setUp(self):
        #öppna connection mot server
        HOST_name = socket.gethostname()
        HOST_ip = socket.gethostbyname(HOST_name)
        PORT = 65432
        global mySocket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
            mySocket.connect((HOST_ip, PORT))
            while True:
                listen_thread = Thread(target=recieve, args=(mySocket,))
                listen_thread.start()
            
    def recieve(mySocket):
        while True:
            data = mySocket.recv(1024).decode('utf-8')
            if not data:
                break
            print(data)
            global answer
            answer= data



    def test_send_msg(self):
        #skicka ett meddelande till server o få samma tillbaks
        message= '%' + 'hejsan'
        b = bytes(message, 'utf-8')
        mySocket.sendall(b)


    def tearDown(self):
        #close connection
     




if __name__ == "__main__":
    unittest.main()
