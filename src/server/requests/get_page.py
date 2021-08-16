import socket
from struct import pack

def getPage(client: socket.socket):
    print("> GetPage")
    client.send(pack("!i", 4))
    for button in ["twitch", "tegh", "maco", "youtube"]:
        with open(f"assets/button_{button}.png", "rb") as buttonFile:
            buffer = buttonFile.read()
            client.send(pack("!i", len(buffer)))
            client.sendall(buffer)
