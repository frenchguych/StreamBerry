import socket
from struct import pack
from typing import Any

from google.protobuf import any_pb2

from proto.streamberry_pb2 import GetPage

def getPage(config: Any, client: socket.socket, anyMessage: any_pb2.Any):
    message = GetPage()
    anyMessage.Unpack(message)
    page = message.page # pylint: disable=no-member
    client.send(pack("!i", 4))
    for button in config['pages'][page]['buttons']:
        with open(f"{button['icon']}", "rb") as buttonFile:
            buffer = buttonFile.read()
            client.send(pack("!i", len(buffer)))
            client.sendall(buffer)
