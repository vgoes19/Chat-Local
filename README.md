# Chat-Python
Comunicação entre cliente servidor com módulo socket 


Principais métodos e funções de Módulo socket Python
socket() 
bind() : associa o socket servidor a um endereço
listen()
accept() : aceita uma conexão de cliente 
connect() : conecta um cliente a um endereço
connect_ex() : idem anterior, retornando um indicador erro, em vez de uma execeção, na ocorrência da chamada do connect em baixo nível 
send()
recv()
close() : fecha um socket, liberando todos os recursos alocados
getpeername() : retorna o endereço do socket remoto com qual um socket local está associado
getsockname() : retorna o endereço do socket local



Métodos para envio e leitura de bytes 
recv(bufsize[, flags]): lê os bytes recebidos, retornando-os em uma string, até o limite de buffer definido por buffsize
recvfrom(bufsize[, flags]): (UDP) lê os bytes recebidos, retornando-os em uma string, até o limite de buffer definido por buffsize
send(bytes[, flags]): solicita o envio dos bytes pelo socket até que um certo conjunto de bytes seja enviado - buffer suficiente para garantir o envio
sendall(bytes[, flags]): envia todos os bytes passados como parâmetro, o que ocasiona sucessivos envios em chamadas de sistema até que todos os bytes sejam enviados
