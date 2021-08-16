import socket
from typing import Any
from zeroconf import ServiceInfo, Zeroconf


def bindSocket(config: Any) -> socket.socket:
    address: str = "0.0.0.0"
    port: int = 0

    if "bind" in config:
        if "address" in config["bind"]:
            address = config["bind"]["address"]
        if "port" in config["bind"]:
            port = config["bind"]["port"]

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
    )
    sock.bind((address, port))

    return sock

def registerService(sock: socket.socket, backlog: int) -> None:
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
    print(f"StreamBerry Server is available at {address}:{port}")
