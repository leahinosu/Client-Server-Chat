"""
References:
Real Python https://realpython.com/python-sockets/
GeeksForGeeks https://www.geeksforgeeks.org/simple-chat-room-using-python/
StackOverflow https://stackoverflow.com/questions/17667903/python-socket-receive-large-amount-of-data
StackOverflow https://stackoverflow.com/questions/275018/how-do-i-remove-a-trailing-newline
"""

import socket
import sys

class Client:
    BUF_SIZE = 256
    QUIT_SYM = b'/q'

    def __init__(self, host, port):
        """
        host: str. host address
        port: int. port number
        isQuit: bool. True if user typed Client.Quit_SYM. False Otherwise.
        """
        self.host = host
        self.port = port
        self.isQuit = False

    def run(self):
        """
        Connect to the chat server.
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.host, self.port))
            
            # Read welcome message
            self.receive(sock)
       
            while True:
                try:
                    self.sendMessage(sock)
                    if self.isQuit:
                        break
                    self.receive(sock)
                except:
                    print("Socket error occured.")
                    break

    def receive(self, sock):
        """
        Receive message from server and print it.
        """
        # Receive length of next mesage from server
        lenMessage = int(sock.recv(self.BUF_SIZE))
        message = b''
        while len(message) < lenMessage:
            recvMessage = sock.recv(self.BUF_SIZE)
            message += recvMessage
        print(message.decode('utf-8'))

    def sendMessage(self, sock):
        """
        Takes message to send from user and send it to server.
        """
        sys.stdout.write(">")
        sys.stdout.flush()
        messageToSend = sys.stdin.readline().strip().encode('utf-8')
        sock.send(str(len(messageToSend)).encode('utf-8'))  # send message length first
        sock.sendall(messageToSend)

        if messageToSend == self.QUIT_SYM:
            self.isQuit = True


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print("Usage: python client.py host port")
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])
        c = Client(host, port)
        c.run()