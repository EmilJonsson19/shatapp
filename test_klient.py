import unittest
import socket
import klientprogram as kp


class testCases(unittest.TestCase):

    HOST_name = socket.gethostname()
    HOST_ip = socket.gethostbyname(HOST_name)
    PORT = 65432

    def test_klient_server_conn(self):
        connection= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((self.HOST_ip,self.PORT))
        message= "&&close"
        connection.send(message.encode('utf-8'))
        recive= connection.recv(1024).decode('utf-8')
        connection.close()
        
        self.assertEqual(message,recive)

    def test_check_if_duplicates(self):
        listan= [1,2,3]
        listan2= [1,2,3,1]
        result= kp.check_if_duplicates(listan2)
        self.assertEqual(result,listan)

  
     




if __name__ == "__main__":
    unittest.main()
