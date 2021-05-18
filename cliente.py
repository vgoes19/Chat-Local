import socket 
import threading

user_name = input("USERNAME: ") #insere o nome de usuario

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 50505)) 
print("teste erro entre branches")

def recebe_mensagem():
    while True:
        try:
            mensagem_recebida = client.recv(1024).decode('ascii') 
            # verifica se o parâmetro passado é o username ou uma mensagem qualquer
            if mensagem_recebida == 'USERNAME':
                client.send(user_name.encode('ascii'))
            else:
                print(mensagem_recebida)
            
        except:
            print("Ocorreu um erro !")
            client.close()
            break


def escreve_mensagem():
    while True:
        mensagem_enviada = f'{user_name}: {input("")}'
        client.send(mensagem_enviada.encode('ascii'))
        print("teste2")
        print('nova atualizacao teste')

recebe_thread = threading.Thread(target=recebe_mensagem)
recebe_thread.start()

escreve_thread = threading.Thread(target=escreve_mensagem)
escreve_thread.start()
