import socket


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    IP = s.getsockname()[0]
    s.close()
    return IP


HOST = "201.69.127.235"
PORT = 5000      

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    USER_ID = "alanrios" + "|" + "Google_Colab" + "|"

    s.connect((HOST, PORT))
    s.send(str.encode(USER_ID + "Colab é toop"))

    while True:
        data = s.recv(1024).decode()
        print('Received', repr(data))
