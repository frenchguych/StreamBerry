import sys

from typing import Any, Callable, Dict

from google.protobuf import any_pb2
from google.protobuf.descriptor import Descriptor
from common.socket_wrapper import SocketWrapper
from server.config import readConfig
from server.network import bindSocket, registerService
from server.requests.get_page import getPage
from proto.streamberry_pb2 import GetPage

if __name__ == "__main__":

    config = readConfig()
    sock = bindSocket(config)
    registerService(sock, 1)

    requestsMap: Dict[Descriptor, Callable[[Any, SocketWrapper, any_pb2.Any], None]] = {
        GetPage.DESCRIPTOR: getPage
    }

    try:
        while True:
            print("Waiting for a client to connect")
            (client, addr) = sock.accept()
            print("Connection from client")
            with client:
                # data = client.recv(2048)
                data = client.recv()
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

    except KeyboardInterrupt:
        pass
    finally:
        print("Exiting")
        sys.exit(0)
