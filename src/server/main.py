import sys

from google.protobuf import any_pb2
from server.config import readConfig
from server.network import bindSocket, registerService
from server.requests import getPage
from proto.streamberry_pb2 import GetPage

if __name__ == "__main__":

    config = readConfig()
    sock = bindSocket(config)
    registerService(sock, 1)

    try:
        while True:
            print("Waiting for a client to connect")
            (client, addr) = sock.accept()
            print("Connection from client")
            with client:
                data = client.recv(2048)
                if not data:
                    break
                message = any_pb2.Any()
                message.ParseFromString(data)

                if message.Is(GetPage.DESCRIPTOR):  # pylint: disable=no-member
                    getPage(client)

    except KeyboardInterrupt:
        pass
    finally:
        print("Exiting")
        sys.exit(0)
