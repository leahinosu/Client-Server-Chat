# Client-Server Chat

## About The Project
A simple client-server chat program using Python's `socket` and `sys` standard libraries.<br/>
The program uses a TCP socket connection to send and receive messages from two different processes.<br/>
The server and client processes verify the length of the received messages by sending the length of the message first.<br/>
They sent the length of the message first because it is lighter compared to the full message, which is larger and has<br/>
a higher chance of being dropped when sent over the network.

This is the final project of Oregon State University's CS372 Introduction to Computer Networks.

## Getting Started

1. Clone the repository to your local machine:
```
git clone https://github.com/leahinosu/Client-Server-Chat
```
2. Open a terminal and run the server program. The example uses port number 5050:
```
python server.py 0.0.0.0 5050
```
3. Open another terminal and run the client program. Ensure the port number matches with the server's:
```
python client.py 127.0.0.1 5050
```
4. If both the server and client connect successfully, you will see "Enter messages to send..." from the client process and "Waiting for message..." from the server process.

<div align="center">
  <img src="https://github.com/user-attachments/assets/dbd3c30c-469b-4512-80e0-91f621e2a95e" alt="Client Chat">
  <p>The client program saying "Hello" to the server</p>
  <img src="https://github.com/user-attachments/assets/61043668-aff2-4792-95cc-9e11bd899fc0" alt="Server Chat">
  <p>The server program responding with "Hi from the server" to the client</p>
</div>
