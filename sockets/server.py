#servidor

# server.py
from socket import * #Isso importa todas as funções do módulo "socket"
                     #Ai não precisamos mais fazer socket.socket.(...)
                     #basta o nome da função/classe direto, no caso socket(...)

from time import asctime,sleep #Mesma coisa, porém agora so importamos a funçao
                                #asctime e sleep do modulo time
                                #dessa forma n precisamos escrever time.time()
                                #ou time.asctime(), basta time() ou asctime()

import os,sys #Importando o módulo os e sys

#Cria o nosso objeto socket (inicializa/instancia) 
server = socket(AF_INET,SOCK_STREAM)
#Nome da nossa máquina
host = gethostname()
port = 9999
#Ativa o socket
server.bind((host, port))
#O servidor está aceitando novas conexões 
server.listen()

def recebe(sckt):
    return sckt.recv(1024).decode('utf8') #Func p/ receber msgs
def envia(sckt, msg):
    sckt.send(msg.encode('utf8')) #Func p/ enviar msgs

print("Em espera...")
# Aceita uma conexão (fica aguardando por uma conexão)
client,addr = server.accept() #cliente = socket p/ cliente / addr = endereço
print("Conexão recebida de: %s" % str(addr)) 
envia(client,'Conexão ativa!')
tempo = asctime() #Pega a data e hora atuais
login = os.getlogin() #Pega o usuário atual do windows
cores = str(os.cpu_count()) #Quantidade de cores do procesador
versao = ('Windows ' + str(sys.getwindowsversion().major) #Versão do windows
+ ' Build ' + str(sys.getwindowsversion().build)) 
dirct = os.getcwd() #Diretório do servidor
pid = str(os.getpid()) #ID do processo atual do servidor
tuser = str(os.times().user)
tos = str(os.times().system)

while True: #Loop infinito
    ordem = recebe(client) #Aguarda a opção do cliente 
    if ordem == '1':
        envia(client, tempo)
    elif ordem == '2':
        envia(client, login)
    elif ordem == '3':
        envia(client, cores)
    elif ordem == '4':
        envia(client, versao)
    elif ordem == '5':
        envia(client, dirct)
    elif ordem == '6':
        envia(client, pid)
    elif ordem == '7':
        os.system('calc.exe') #Abre a calculadora
        envia(client,'Aberto com sucesso!')
    elif ordem == '8':
        os.system('py') #Abre o interpretador python pelo cmd 
        envia(client,'Aberto com sucesso!')
    elif ordem == '9':
        envia(client,tuser)
    elif ordem == '10':
        envia(client,tos)
    elif ordem == '0': 
        client.close()
        server.close()
        print('Saindo da aplicação...')
        sleep(2) #Espera 2 segundos
        break
        
        
    
