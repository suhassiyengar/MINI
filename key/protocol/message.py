import json

def create_message(msg_type, data):
    return json.dumps({
        "type": msg_type,
        "data": data
    }).encode()

def parse_message(msg):
    return json.loads(msg.decode())