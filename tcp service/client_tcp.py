import socket

IP = '127.0.0.1'
PORT = 9998

def send_message(message):
    """ Envoie un message au serveur """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT))
    client.send(message.encode('utf-8'))
    response = client.recv(4096)
    print(f'Réponse du serveur : {response.decode("utf-8")}')
    client.close()

if __name__ == '__main__':
    print(f"\n--- Envoyez un message à {IP}:{PORT} ou écrivez 'quit' pour quitter ---\n")
    while True:
        message = input("Entrez un message : ")
        if message.lower() == 'quit':
            break
        send_message(message)
