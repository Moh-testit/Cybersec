import socket

IP = '127.0.0.1'
PORT = 9999

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (IP, PORT)

    while True:
        message = input("Entrez un message à envoyer (ou 'quit' pour quitter) : ")
        if message.lower() == 'quit':
            break
        client_socket.sendto(message.encode('utf-8'), server_address)
        data, server = client_socket.recvfrom(4096)
        print(f"Réponse du serveur : {data.decode('utf-8')}")

    client_socket.close()

if __name__ == '__main__':
    main()
    