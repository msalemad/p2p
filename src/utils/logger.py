import os
import logging
from datetime import datetime

# Configure logging
log_file_path = os.path.join(os.path.dirname(__file__), '../../log.txt')
logging.basicConfig(
    filename=log_file_path,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_info(message):
    logging.info(message)
    print(f"\033[92m[INFO] {message}\033[0m")  # Green text

def log_warning(message):
    logging.warning(message)
    print(f"\033[93m[WARNING] {message}\033[0m")  # Yellow text

def log_error(message):
    logging.error(message)
    print(f"\033[91m[ERROR] {message}\033[0m")  # Red text

def log_connection(client_ip, client_name, os_version):
    log_info(f"Client connected: IP={client_ip}, Name={client_name}, OS={os_version}")

def log_file_transfer(file_name, bytes_transferred, total_bytes):
    percentage = (bytes_transferred / total_bytes) * 100
    log_info(f"Transferring file: {file_name} | Progress: {percentage:.2f}% | Bytes transferred: {bytes_transferred}/{total_bytes}")