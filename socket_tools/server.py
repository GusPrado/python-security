import socket

app_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso!')

host = "localhost"
port = 5432

app_socket.bind((host, port))
message = "\nServidor: I'm here!!"

while 1:
    data, end = app_socket.recvfrom(4096)

    if data:
        print("Servidor enviando mensagem...")
        app_socket.sendto((message.encode()), end)
