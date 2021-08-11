import socket
import sys
from os import environ, path
from struct import pack

import yaml
from google.protobuf import any_pb2
from zeroconf import ServiceInfo, Zeroconf
from proto.streamberry_pb2 import GetPage

if __name__ == "__main__":
    config_files = [
        file
        for file in [
            "streamberry.yaml",
            f"{environ['HOME']}/.config/streamberry/streamberry.yaml",
        ]
        if path.exists(file)
    ]

    if "SNAP_USER_COMMON" in environ:
        config_file = path.join(environ['SNAP_USER_COMMON'], 'streamberry.yaml')
        if path.exists(config_file):
            config_files.append(config_file)

    if len(config_files) == 0:
        raise FileNotFoundError("streamberry.yaml")

    with open(config_files[0], "r") as stream:
        config = yaml.safe_load(stream)

    if config is None or "pages" not in config:
        raise KeyError("Key 'pages' not found in config file")

    root = path.dirname(config_files[0])
    root = "./" if root == "" else root

    pages = config["pages"]

    index: int = 0
    for page in pages:
        for button in page["buttons"]:
            button['icon'] = path.join(root, button['icon'])
            if not path.exists(button['icon']):
                raise FileNotFoundError(button['icon'])

    print(pages)

    address: str = "0.0.0.0"
    port: int = 0

    if "bind" in config:
        print(config["bind"])
        if "address" in config["bind"]:
            address = config["bind"]["address"]
        if "port" in config["bind"]:
            port = config["bind"]["port"]

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
    )
    sock.bind((address, port))
    sock.listen(1)
    (
        ip,
        port,
    ) = sock.getsockname()

    info = ServiceInfo(
        "_streamberry._tcp.local.",
        "Stream Berry Server._streamberry._tcp.local.",
        addresses=[
            socket.inet_pton(
                socket.AF_INET,
                ip,
            )
        ],
        port=port,
    )

    zeroconf = Zeroconf()
    zeroconf.register_service(info)
    print(f"StreamBerry Server is available at {ip}:{port}")

    try:
        while True:
            print("Waiting for a client to connect")
            (
                client,
                addr,
            ) = sock.accept()
            print("Connection from client")
            with client:
                data = client.recv(2048)
                if not data:
                    break
                message = any_pb2.Any()
                message.ParseFromString(data)

                if message.Is(GetPage.DESCRIPTOR):  # pylint: disable=no-member
                    print("> GetPage")
                    client.send(
                        pack(
                            "!i",
                            4,
                        )
                    )
                    for button in [
                        "twitch",
                        "tegh",
                        "maco",
                        "youtube",
                    ]:
                        with open(
                            f"assets/button_{button}.png",
                            "rb",
                        ) as f:
                            b = f.read()
                        client.send(
                            pack(
                                "!i",
                                len(b),
                            )
                        )
                        client.sendall(b)
    except KeyboardInterrupt:
        pass
    finally:
        print("Exiting")
        sys.exit(0)
