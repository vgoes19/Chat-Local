import threading
import socket

host = '127.0.0.1' # localhost
port = 50505 

#Interface de soquetes de fluxo (stream): Define um serviço orientado à conexão confiável (sobre TCP)
#Dados são enviados sem erros ou duplicação, e recebidos na mesma ordem em que foram enviados. SOCK_STREAM

#Criação de um objeto do tipo socket usando o método socket.socket(), o qual recebe dois parâmetros ->
# 1- Família de endereços (AF_INET (endereço IPv4))
# 2- Tipo de socket (SOCK_STREAM)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port)) # apenas um parâmetro = (())
server.listen()

#Declaração de listas
clients = []
user_names = []

def trasmissao_mensagem(mensagem):
    for client in clients:
        client.send(mensagem)


def recebe_mensagem(client):
    while True:
        try:
            #recebe e envia mensagem a todos os clientes conectados
            mensagem = client.recv(1024) #recebe até 1024 bytes de dados
            trasmissao_mensagem(mensagem)
        except:
            #trata erro de mensagem recebida de cliente
            index = clients.index(client)
            #busca o client que houve o erro e fecha sua conexão
            clients.remove(client)
            client.close()
            user_name = user_names[index]
            trasmissao_mensagem(f'{user_name} se desconectou !')
            #também é removido das listas (clients e user_names)
            user_names.remove(user_name)
            break

def aceita_conexao():
    
    while True:
        client, address = server.accept()
        print(f"Conexao com {str(address)}")

        client.send('USERNAME'.encode('ascii')) #ascii -> codificação binária para caracteres
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
