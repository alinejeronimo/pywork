import socket
import time
import hashlib


MAX_BYTES = 65535
sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 9001


menu = '''
  --- Sistema de Arquivos ---
  0. Sair
  1. Acessar arquivo
   '''

def rcv():
	status, address = sckt.recvfrom(MAX_BYTES)
	if int(status.decode('utf-8')):
	    arq, address = sckt.recvfrom(MAX_BYTES)
	    hashArq, address = sckt.recvfrom(MAX_BYTES)
	    arq = arq.decode('utf-8')
	    hashArq = hashArq.decode('utf-8')
	    h = hashlib.sha512()
	    h.update(arq.encode('utf-8'))
	    h = h.hexdigest()
	    f = open('recebido.txt', 'w')
	    f.write(arq)
	    if hashArq == h:
	        print("Arquivo íntegro, salvo com sucesso em 'recebido.txt'! \nConteúdo: %s" %arq)
	    else:
	        print('Arquivo não íntegro')
	else:
		print("Arquivo não encontrado")


while True:
    print(menu)
    opc = input("Opção: ")
    if opc == '1':
        data = '1'.encode('utf-8')
        sckt.sendto(data, (host, port))
        d, a = sckt.recvfrom(MAX_BYTES)
        itens, a = sckt.recvfrom(MAX_BYTES)
        itens = itens.decode('utf-8')
        itens = itens.split()
        print('Arquivos Disponíveis:\n')
        for i in itens:
                print('%s' %i)
        cons = input("Nome do arquivo: ")
        cons = cons.encode('utf-8')
        sckt.sendto(cons, a)
        rcv()
    elif opc == '0':
        print("Encerrando aplicação...")
        time.sleep(3)
        break
    else:
        print('Opção inválida!')
        continue
