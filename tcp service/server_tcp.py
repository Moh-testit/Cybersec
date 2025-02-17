import socket
import threading

IP = '0.0.0.0'  # Accepte les connexions depuis n'importe quelle IP
PORT = 9998

def handle_client(client_socket):
    """ Gère la communication avec un client """
    with client_socket as sock:
        data = sock.recv(1024)
        print(f'[*] Reçu: {data.decode("utf-8")}')
        sock.send(b'200 - OK')

def main():
    """ Crée et exécute le serveur """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Serveur en écoute sur {IP}:{PORT}')

    while True:
        client, address = server.accept()
        print(f'[*] Connexion acceptée de {address[0]}:{address[1]}')
        client_thread = threading.Thread(target=handle_client, args=(client,))
        client_thread.start()

if __name__ == '__main__':
    main()
