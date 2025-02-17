import socket

HOST = '127.0.0.1'  # Adresse du serveur (localhost)
PORT = 65432        # Port du serveur

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Bonjour, serveur')
    data = s.recv(1024)

print(f"Reçu du serveur : {data.decode()}")
