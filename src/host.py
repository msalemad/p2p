import socket
import os
import threading
from utils.logger import log_info, log_error

class Host:
    def __init__(self):
        self.server_socket = None
        self.clients = []

    def setup_server(self, port=0):
        if port == 0:
            port = self.recommend_port()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('', port))
        self.server_socket.listen(5)
        log_info(f"Server listening on port {port}")

    def recommend_port(self):
        return 8080  # Example of a recommended port

    def accept_connections(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            self.clients.append(client_socket)
            log_info(f"Client connected: {addr}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        try:
            client_info = client_socket.recv(1024).decode()
            log_info(f"Client info: {client_info}")
            self.send_file_list(client_socket)
        except Exception as e:
            log_error(f"Error handling client: {e}")
        finally:
            client_socket.close()

    def send_file_list(self, client_socket):
        files = os.listdir('output')
        client_socket.send('\n'.join(files).encode())
        log_info("Sent file list to client")

    def start(self):
        port = int(input("Enter port to use (or press Enter for recommended): ") or 0)
        self.setup_server(port)
        self.accept_connections()

if __name__ == "__main__":
    host = Host()
    host.start()