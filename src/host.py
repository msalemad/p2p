import socket
import threading

def handle_client(client_socket):
    # Manejar la conexión del cliente
    pass

def run():
    print("Iniciando el módulo Host...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 0))
    server.listen(5)
    print(f"Servidor escuchando en {server.getsockname()}")

    while True:
        client_socket, addr = server.accept()
        print(f"Cliente conectado: {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    run()