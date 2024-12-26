import os
import sys

# Asegurarse de que el directorio src esté en el path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def main():
    print("Bienvenido a la aplicación de intercambio de archivos P2P")
    print("Seleccione una opción:")
    print("1. Enviar archivos como Host")
    print("2. Recibir archivos como Client")
    
    choice = input("Ingrese el número de su elección: ")
    
    if choice == '1':
        import host
        host.run()
    elif choice == '2':
        import client
        client.run()
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        sys.exit(1)

if __name__ == "__main__":
    main()