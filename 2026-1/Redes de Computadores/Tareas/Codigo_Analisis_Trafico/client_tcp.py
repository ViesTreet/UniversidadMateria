import socket
import time

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5000
NUM_MESSAGES = 5
DELAY_SECONDS = 1
MESSAGE_SIZE = 50

MESSAGE_BODY = "X" * MESSAGE_SIZE

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, SERVER_PORT))

start_time = time.time()

for i in range(NUM_MESSAGES):
    msg = f"MSG {i}: {MESSAGE_BODY}"
    send_time = time.time()
    sock.sendall(msg.encode())
    sock.recv(1024)
    rtt = time.time() - send_time
    print(f"RTT mensaje {i}: {rtt:.4f} s")
    time.sleep(DELAY_SECONDS)

print(f"Tiempo total: {time.time() - start_time:.2f} s")
sock.close()
