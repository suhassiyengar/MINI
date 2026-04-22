import socket
import threading
import json

HOST = "0.0.0.0"
PORT = 5000
AUTH_TOKEN = "iot_secure_key"

devices = {}

def handle_device(conn, addr):
    print(f"Device connected: {addr}")

    try:
        # AUTH
        auth_data = conn.recv(1024).decode()

        if auth_data.startswith("AUTH"):
            token = auth_data.split()[1]

            if token == AUTH_TOKEN:
                conn.send("AUTH_SUCCESS".encode())
                print("Device authenticated")
            else:
                conn.send("AUTH_FAIL".encode())
                conn.close()
                return

        devices[addr] = conn

        while True:
            msg = conn.recv(1024)
            if not msg:
                break

    except Exception as e:
        print("Error:", e)

    finally:
        print("Device disconnected:", addr)
        conn.close()
        devices.pop(addr, None)


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Controller running on port 5000...")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_device, args=(conn, addr), daemon=True).start()


def send_command(command):
    results = []

    for addr, conn in devices.items():
        try:
            msg = json.dumps({
                "type": "command",
                "command": command
            }).encode()

            conn.send(msg)

            response = conn.recv(1024).decode()
            data = json.loads(response)
            results.append(f"{addr} → {data['result']}")

        except Exception as e:
            results.append(f"{addr}: Error {str(e)}")

    return "<br>".join(results) if results else "No devices connected"