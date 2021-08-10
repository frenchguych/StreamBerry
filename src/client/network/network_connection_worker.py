import socket
import threading
from typing import Callable

from zeroconf import Zeroconf

from toolkit import BaseWorker


class NetworkConnectionWorker(BaseWorker):
    def __init__(self, finishedHandler: Callable[[str, int], None]) -> None:
        super().__init__()
        self.finishedHandler = finishedHandler

    def run(self) -> None:
        zeroconf = Zeroconf()
        serviceinfo = zeroconf.get_service_info(
            "_streamberry._tcp.local.", "Stream Berry Server._streamberry._tcp.local."
        )

        address: str = ""
        port: int = 0

        if serviceinfo is not None:
            address = socket.inet_ntop(socket.AF_INET, serviceinfo.addresses[0])
            port = serviceinfo.port

        self.stop()
        self.finishedHandler(address, port)
