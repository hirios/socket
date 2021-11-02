import socket
import threading 


HOST = "192.168.15.120" #socket.gethostbyname(socket.gethostname())
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

CLIENTES = []
while True:
    conn, addr = server.accept()
    print('Connected by', addr)
    conn.send(str.encode("CONEXÃO SUCEDIDA", "UTF-8"))
    
    CLIENTES.append(conn)

    data = conn.recv(2048)
    if data:     
        if data.decode() == "sinal":
            for c in CLIENTES:
                    try:
                        # EXCEÇÃO CASO A CONEXAO SEJA FECHADA
                        c.send(str.encode("PERFEITO", "UTF-8"))
                    except:
                        print("A CONEXÃO PROVAVELMENTE FOI FECHADA")
