import sys
from zeroconf import ServiceInfo, Zeroconf
import zeroconf
import socket
from proto.streamberry_pb2 import Ping, Pong
from google.protobuf.any_pb2 import Any

if "__main__" == __name__:
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
        while(True):
            client, addr = sock.accept()

            with client:
                data = client.recv(2048)
                print(data)
                if not data:
                    break
                any = Any()
                any.ParseFromString(data)
                if any.Is(Ping.DESCRIPTOR):
                    ping = Ping()
                    any.Unpack(ping)
                    print("Ping message detected !")
                    print(ping)

    except KeyboardInterrupt:
        pass
    finally:
        print("Exiting")
        sys.exit(0)
