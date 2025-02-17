import socket

IP = '0.0.0.0'
PORT = 9999

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((IP, PORT))

    print(f"Serveur UDP en écoute sur {IP}:{PORT}")

    while True:
        data, address = server_socket.recvfrom(1024)
        print(f"Reçu de {address}: {data.decode('utf-8')}")
        server_socket.sendto(b'ACK', address)

if __name__ == '__main__':
    main()
