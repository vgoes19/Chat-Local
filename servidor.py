import threading
import socket

host = '127.0.0.1' # localhost
port = 50505 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port)) 
server.listen()


clients = []
user_names = []

def trasmissao_mensagem(mensagem):
    for client in clients:
        client.send(mensagem)


def recebe_mensagem(client):
    while True:
        try:
            #recebe e envia mensagem a todos os clientes conectados
            mensagem = client.recv(1024) 
            trasmissao_mensagem(mensagem)

        except:

            index = clients.index(client)
            clients.remove(client)
            client.close()
            user_name = user_names[index]
            trasmissao_mensagem(f'{user_name} se desconectou !')
            user_names.remove(user_name)
            break

def aceita_conexao():
    
    while True:
        client, address = server.accept()
        print(f"Conexao com {str(address)}")

        client.send('USERNAME'.encode('ascii')) 
        user_name = client.recv(1024).decode('ascii')
        user_names.append(user_name)
        clients.append(client)

        print(f"USERSNAME IS {user_name}")
        trasmissao_mensagem(f"{user_name} entrou no servidor !".encode('ascii'))
        client.send('Conectado ao servidor !'.encode('ascii'))

        # Diferentes execuções em um mesmo processo 
        thread = threading.Thread(target=recebe_mensagem, args=(client,)) 
        thread.start()

print('O servidor esta escutando...')
aceita_conexao()
