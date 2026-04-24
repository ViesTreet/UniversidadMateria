import socket

SERVER_IP = "0.0.0.0"
SERVER_PORT = 5000
BUFFER_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(1)

print(f"[SERVIDOR] Escuchando en puerto {SERVER_PORT}...")
conn, addr = server_socket.accept()
print(f"[SERVIDOR] Conexión aceptada desde {addr}")

while True:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    message = data.decode()
    response = f"ACK:{message}"
    conn.sendall(response.encode())

conn.close()
server_socket.close()
print("[SERVIDOR] Conexión cerrada.")
