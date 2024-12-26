import socket
import os
import threading
import time
from utils.logger import log_info, log_error

class Client:
    def __init__(self):
        self.host_ip = ""
        self.host_port = 0
        self.connection = None

    def connect_to_host(self):
        self.host_ip = input("Enter the host IP address: ")
        self.host_port = int(input("Enter the host port: "))
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.connection.connect((self.host_ip, self.host_port))
            log_info(f"Connected to host at {self.host_ip}:{self.host_port}")
            self.list_files()
        except Exception as e:
            log_error(f"Connection failed: {e}")

    def list_files(self):
        self.connection.sendall(b'LIST')
        files = self.connection.recv(1024).decode().splitlines()
        print("Files available for download:")
        for idx, file in enumerate(files):
            print(f"{idx + 1}: {file}")

        choice = input("Enter the number of the file to download (or 'exit' to quit): ")
        if choice.lower() == 'exit':
            self.connection.close()
            return
        self.download_file(files[int(choice) - 1])

    def download_file(self, filename):
        self.connection.sendall(f'DOWNLOAD {filename}'.encode())
        file_size = int(self.connection.recv(1024).decode())
        self.connection.sendall(b'READY')

        with open(os.path.join('input', filename), 'wb') as f:
            bytes_received = 0
            start_time = time.time()
            while bytes_received < file_size:
                data = self.connection.recv(1024)
                f.write(data)
                bytes_received += len(data)
                elapsed_time = time.time() - start_time
                speed = bytes_received / elapsed_time if elapsed_time > 0 else 0
                print(f"Downloaded {bytes_received} of {file_size} bytes. Speed: {speed:.2f} bytes/sec")

        log_info(f"Downloaded {filename} successfully.")
        self.connection.close()

if __name__ == "__main__":
    client = Client()
    client.connect_to_host()