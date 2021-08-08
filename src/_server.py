import sys
import socket

from zeroconf import ServiceInfo, Zeroconf
from google.protobuf import any_pb2

from proto.streamberry_pb2 import Ping

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
            client, addr = sock.accept()

            with client:
                data = client.recv(2048)
                print(data)
                if not data:
                    break
                message = any_pb2.Any()
                message.ParseFromString(data)
                if message.Is(Ping.DESCRIPTOR): # pylint: disable=no-member
                    ping = Ping()
                    message.Unpack(ping) # pylint: disable=no-member
                    print("Ping message detected !")
                    print(ping)

    except KeyboardInterrupt:
        pass
    finally:
        print("Exiting")
        sys.exit(0)
