import socket

app_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso!")

host = "localhost"
port = 5433
message = "Hello server"

try:
    print("Cliente: ", message)
    app_socket.sendto(message.encode(), (host, 5432))

    data, server = app_socket.recvfrom(4096)
    data = data.decode()

    print("Cliente: " + data)
finally:
    print("Cliente: Encerrando a conexão")
    app_socket.close()
