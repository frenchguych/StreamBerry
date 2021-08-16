import sys
import socket

from typing import Any, Callable

from google.protobuf import any_pb2
from google.protobuf.descriptor import Descriptor
from server.config import readConfig
from server.network import bindSocket, registerService
from server.requests import getPage
from proto.streamberry_pb2 import GetPage

if __name__ == "__main__":

    config = readConfig()
    sock = bindSocket(config)
    registerService(sock, 1)

    requestsMap: dict[Descriptor, Callable[[Any, socket.socket, any_pb2.Any], None]] = {
        GetPage.DESCRIPTOR: getPage
    }

    try:
        while True:
            print("Waiting for a client to connect")
            (client, addr) = sock.accept()
            print("Connection from client")
            with client:
                data = client.recv(2048)
                if not data:
                    break
                anyMessage = any_pb2.Any()
                anyMessage.ParseFromString(data)

                handlers = [
                    handler
                    for (descriptor, handler) in requestsMap.items()
                    if anyMessage.Is(descriptor) # pylint: disable=no-member
                ]

                if handlers is not None and len(handlers) == 1:
                    handler = handlers[0]
                    handler(config, client, anyMessage)
                #if message.Is(GetPage.DESCRIPTOR):  # pylint: disable=no-member
                #    getPage(client)

    except KeyboardInterrupt:
        pass
    finally:
        print("Exiting")
        sys.exit(0)
