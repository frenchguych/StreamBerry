import sys

from typing import Callable, Dict

from google.protobuf import any_pb2
from google.protobuf.descriptor import Descriptor
from common.socket_wrapper import SocketWrapper
from server.config import Config, readConfig
from server.network import bindSocket, registerService
from server.requests.get_page import getPage
from server.requests.button_clicked import buttonClicked
from proto.streamberry_pb2 import ButtonClicked, GetPage

if __name__ == "__main__":

    config = readConfig()
    sock = bindSocket(config)
    registerService(sock, 1)

    requestsMap: Dict[Descriptor, Callable[[Config, SocketWrapper, any_pb2.Any], None]] = {
        GetPage.DESCRIPTOR: getPage,
        ButtonClicked.DESCRIPTOR: buttonClicked,
    }

    try:
        (client, addr) = sock.accept()
        with client:
            while True:
                # data = client.recv(2048)
                data = client.recv()
                if not data:
                    break
                anyMessage = any_pb2.Any()
                anyMessage.ParseFromString(data)

                handlers = [
                    handler
                    for (descriptor, handler) in requestsMap.items()
                    if anyMessage.Is(descriptor)
                ]

                if handlers is not None and len(handlers) == 1:
                    handler = handlers[0]
                    handler(config, client, anyMessage)

    except KeyboardInterrupt:
        pass
    finally:
        sys.exit(0)
