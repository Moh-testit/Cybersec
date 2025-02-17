import socket

HOST = '127.0.0.1'  # Adresse loopback (localhost)
PORT = 65432        # Port d'écoute (les ports > 1023 sont généralement non privilégiés)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Serveur en écoute sur {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Connecté par {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Reçu : {data.decode()}")
            conn.sendall(data)
