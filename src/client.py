import socket

def run():
    print("Iniciando el módulo Client...")
    server_ip = input("Ingrese la IP del servidor: ")
    server_port = int(input("Ingrese el puerto del servidor: "))

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))
    print(f"Conectado al servidor en {server_ip}:{server_port}")

    # Código para manejar la descarga de archivos
    pass

if __name__ == "__main__":
    run()