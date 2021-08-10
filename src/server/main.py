from struct import pack
import sys
import socket

from zeroconf import ServiceInfo, Zeroconf
from google.protobuf import any_pb2

from proto.streamberry_pb2 import GetPage

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("0.0.0.0", 0))
    sock.listen(1)
    ip, port = sock.getsockname()

    info = ServiceInfo(
        '_streamberry._tcp.local.',
        'Stream Berry Server._streamberry._tcp.local.',
        addresses=[socket.inet_pton(socket.AF_INET, ip)],
        port=port
    )

    zeroconf = Zeroconf()
    zeroconf.register_service(info)

    try:
        while True:
            print("Waiting for a client to connect")
            client, addr = sock.accept()
            print("Connection from client")
            with client:
                data = client.recv(2048)
                if not data:
                    break
                message = any_pb2.Any()
                message.ParseFromString(data)

                if message.Is(GetPage.DESCRIPTOR): # pylint: disable=no-member
                    print("> GetPage")
                    client.send(pack("!i", 4))
                    for button in ["twitch", "tegh", "maco", "youtube"]:
                        with open(f"assets/button_{button}.png", "rb") as f:
                            b = f.read()
                        client.send(pack("!i", len(b)))
                        client.sendall(b)
    except KeyboardInterrupt:
        pass
    finally:
        print("Exiting")
        sys.exit(0)
