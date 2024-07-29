"""
References:
Real Python https://realpython.com/python-sockets/
GeeksForGeeks https://www.geeksforgeeks.org/simple-chat-room-using-python/
StackOverflow https://stackoverflow.com/questions/17667903/python-socket-receive-large-amount-of-data
StackOverflow https://stackoverflow.com/questions/275018/how-do-i-remove-a-trailing-newline
"""

import socket
import sys

class Server:
    BUF_SIZE = 256
    QUIT_SYM = b'/q'

    def __init__(self, host, port):
        """
        host: str. host address
        port: int. port number
        isQuit: bool. True if client sent Server.QUIT_SYM. False Otherwise.
        """
        self.host = host
        self.port = port
        self.isQuit = False

    def run(self):
        """
        Start listening and accepting a client.
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listeningSocket:          
            listeningSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            listeningSocket.bind((self.host, self.port))
            listeningSocket.listen()
            print("Server listening on: " + self.host + " on port: " + str(self.port))
            conn, addr = listeningSocket.accept()
            print ("Connected by ('" + addr[0] +"', " + str(addr[1]) + ")")

            with conn:
                self.sendIntro(conn)
                print("Waiting for message...")

                while True:
                    try:
                        self.receive(conn, addr)
                        if self.isQuit:
                            break
                        self.sendMessage(conn)
                    except:
                        print("Socket error occured.")
                        break

    def sendIntro(self, conn):
        """
        Send the first message to newly accepted client.
        """
        intro = b"Type /q to quit.\nEnter message to send..."
        conn.send(str(len(intro)).encode('utf-8'))
        conn.sendall(intro)

    def receive(self, conn, addr):
        """
        Receive and print message from client.
        """
        # Receive length of next message from client
        lenMessage = int(conn.recv(self.BUF_SIZE))
        message = b''
        while len(message) < lenMessage:
            recvMessage = conn.recv(self.BUF_SIZE)
            message += recvMessage

        if message and message != self.QUIT_SYM:
            print(addr[0] +": " + message.decode('utf-8'))
        else:
            self.isQuit = True
            
    def sendMessage(self, conn):
        """
        Tkaes message from user and send it to client.
        """
        sys.stdout.write(">")
        sys.stdout.flush()
        messageToSend = sys.stdin.readline().strip().encode('utf-8')
        conn.send(str(len(messageToSend)).encode('utf-8'))  # send message length first
        conn.sendall(messageToSend)                     


if __name__ == '__main__': 
    
    if len(sys.argv) < 3:
        print("Usage: python server.py host port")
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])
        s = Server(host, port)
        s.run()