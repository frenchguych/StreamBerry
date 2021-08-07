from typing import Callable

from toolkit.core.BaseWorker import BaseWorker
from zeroconf import Zeroconf


class NetworkConnectionWorker(BaseWorker):
    def __init__(self, finishedHandler: Callable) -> None:
        super().__init__()
        self.finishedHandler = finishedHandler

    def run(self) -> None:
        zeroconf = Zeroconf()
        serviceinfo = zeroconf.get_service_info(
            "_streamberry._tcp.local.", "Stream Berry Server._streamberry._tcp.local."
        )
        print(serviceinfo)
        self.stop()
        self.finishedHandler()
