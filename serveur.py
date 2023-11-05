import socket
import os
import re
from dotenv import load_dotenv

from route import *
from controller import *


load_dotenv()
listen = int(os.getenv("LISTEN"))
host = os.getenv("HOST")
port = int(os.getenv("PORT"))

def route(path):
    if path in routes:
        return globals()[routes[path]]
    else:
        return None

def create_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(listen)
    print(f"Serveur en écoute sur http://{host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        request_data = client_socket.recv(1024).decode('utf-8')
        request_lines = request_data.split('\r\n')
        request_line = request_lines[0]

        # Utilisez une expression régulière pour extraire l'URL demandée
        match = re.match(r"GET (.+?) HTTP/1.1", request_line)
        if match:
            path = match.group(1)
        else:
            path = "/"

        handler = route(path)

        if handler is not None:
            response_body = handler()
            response_data = f"HTTP/1.1 200 OK\r\nContent-Length: {len(response_body)}\r\n\r\n{response_body}"
        else:
            response_body = "Page non trouvée"
            response_data = f"HTTP/1.1 404 Not Found\r\nContent-Length: {len(response_body)}\r\n\r\n{response_body}"

        client_socket.sendall(response_data.encode('utf-8'))
        client_socket.close()

if __name__ == '__main__':
    create_server()