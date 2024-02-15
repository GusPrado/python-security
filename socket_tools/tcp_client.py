import socket
import sys

def main():
    try:
        create_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as error:
        print("A conexão falhou!")
        print(f"Erro: {error}")
        sys.exit()

    print("Socket criado com sucesso!!")

    target_host = input("Digite o hostname para conexão: ")
    target_port = input("Digite a porta para conexão: ")

    try:
        #target_address = ()
        create_socket.connect((target_host, int(target_port)))
        print(f"Conexão TCP estabelecida com {target_host} na porta {target_port}")
        create_socket.shutdown(2)
    except socket.error as error:
        print(f"Não foi possível conectar com {target_host} na porta {target_port}")
        print(f"Erro: {error}")
        sys.exit()

if __name__ == "__main__":
    main()

    