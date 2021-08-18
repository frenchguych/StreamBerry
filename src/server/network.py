import socket
from zeroconf import ServiceInfo, Zeroconf

from common.socket_wrapper import SocketWrapper
from server.config import Config


def bindSocket(config: Config) -> SocketWrapper:
    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
    )
    sock.bind((config.bind.address, config.bind.port))

    return SocketWrapper(sock)

def registerService(sock: SocketWrapper, backlog: int) -> None:
    sock.listen(backlog)
    (address, port) = sock.getsockname()

    info = ServiceInfo(
        "_streamberry._tcp.local.",
        "Stream Berry Server._streamberry._tcp.local.",
        addresses=[
            socket.inet_pton(
                socket.AF_INET,
                address,
            )
        ],
        port=port,
    )

    zeroconf = Zeroconf()
    zeroconf.register_service(info)
