import socket
import json
import webbrowser

SERVER_IP = "10.20.202.140"
PORT = 5000
TOKEN = "iot_secure_key"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

# AUTH
client.send(("AUTH " + TOKEN).encode())

resp = client.recv(1024).decode()

if resp != "AUTH_SUCCESS":
    print("Auth failed")
    exit()

print("Connected to controller")

while True:
    try:
        msg = client.recv(1024)

        if not msg:
            break

        data = json.loads(msg.decode())
        command = data["command"]

        print("Command received:", command)

        if command == "OPEN_GOOGLE":
            webbrowser.open("https://www.google.com")
            result = "Google opened"

        elif command == "OPEN_YOUTUBE":
            webbrowser.open("https://www.youtube.com")
            result = "YouTube opened"

        elif command == "STATUS":
            result = "Device running"

        else:
            result = "Unknown command"

        response = {
            "result": result,
            "ack": "OK"
        }

        client.send(json.dumps(response).encode())

    except Exception as e:
        print("Error:", e)
        break

client.close()