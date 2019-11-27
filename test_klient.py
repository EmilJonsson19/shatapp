import unittest
import socket
import klientprogram as kp


class testCases(unittest.TestCase):

    """def setUp(self):
        #öppna connection mot server
        HOST_name = socket.gethostname()
        HOST_ip = socket.gethostbyname(HOST_name)
        PORT = 65432
        global mySocket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
            mySocket.connect((HOST_ip, PORT))
            global message
            message= '%' + 'hejsan'
            b = bytes(message, 'utf-8')
            mySocket.sendall(b)
            data = mySocket.recv(1024).decode('utf-8')
            if data[0]=="%":
                print(data)
                global answer
                answer=data
            
            mySocket.close()
        """
                
                    
   

    def test_check_if_duplicates(self):
        listan= [1,2,3]
        listan2= [1,2,3,1]
        result= kp.check_if_duplicates(listan2)
        print(result)
        self.assertEqual(result,listan)


    #def test_send_msg(self):
        #skicka ett meddelande till server o få samma tillbaks
       
        #self.assertEqual(answer,message)


    #def tearDown(self):
        #close connection
        #mySocket.close()
     




if __name__ == "__main__":
    unittest.main()
