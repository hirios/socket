import socket
import threading


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    IP = s.getsockname()[0]
    s.close()
    return IP


HOST = get_ip()
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print('--- SUBINDO SERVIDOR ---')

CLIENTES = {}
while True:
    conn, addr = server.accept()
    conn.send(str.encode("CONEXÃO SUCEDIDA", "UTF-8"))
    print('User IP: ', addr)


    data = conn.recv(2048)
    if data:
        USER_ID, DESTINO, MSG = data.decode().split("|")
        CLIENTES[USER_ID] = {"SESSAO": conn, "destino": DESTINO}

        if DESTINO in CLIENTES and DESTINO != "":
            CLIENTES[DESTINO]["SESSAO"].send(str.encode(MSG))




        # if MSG == "sinal":
        #     for c in CLIENTES:
        #             # EXCEÇÃO CASO A CONEXAO SEJA FECHADA
        #             try:
        #                 c.send(str.encode("PERFEITO", "UTF-8"))
        #             except:
        #                 # REMOVENDO CLIENTE DA LISTA DE CLIENTES CONECTADOS
        #                 CLIENTES.remove(c)
        #                 print("A CONEXÃO PROVAVELMENTE FOI FECHADA")
