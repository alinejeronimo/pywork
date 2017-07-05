import socket
import time
import threading
import hashlib
import os


MAX_BYTES = 65535
sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 9001
sckt.bind((host, 9001))


def server():
    print('Aguardando conexões...')
    while True:
        data, address = sckt.recvfrom(MAX_BYTES)
        opc = data.decode('utf-8')
        t = threading.Thread(target=answer, args=(address, opc))
        t.start()


def answer(address, opc):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto("Conexão estabelecida!".encode('utf-8'), address)
    if opc == '1':
        itens = os.listdir('C:/Users/Alunos/Desktop')
        itens = ' '.join(itens)
        s.sendto(itens.encode('utf-8'), address)
        data, address = s.recvfrom(MAX_BYTES)
        arq = data.decode('utf-8')
        try:
            f = open(arq)
            h = hashlib.sha512()
            d = f.read()
            s.sendto('1'.encode('utf-8'), address)
            data = d.encode('utf-8')
            h.update(data)
            s.sendto(d.encode('utf-8'), address)
            s.sendto(h.hexdigest().encode('utf-8'), address)
        except FileNotFoundError:
            s.sendto('0'.encode('utf-8'),address)


server()
