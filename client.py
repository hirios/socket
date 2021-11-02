import socket


HOST = "192.168.15.120" #socket.gethostbyname(socket.gethostname())
PORT = 5000      

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b"COMPUTADOR")

    while True:
        data = s.recv(1024).decode()
        print('Received', repr(data))





