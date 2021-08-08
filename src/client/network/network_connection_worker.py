from typing import Callable, Optional

from zeroconf import ServiceInfo, Zeroconf

from toolkit import BaseWorker


class NetworkConnectionWorker(BaseWorker):
    def __init__(
        self, finishedHandler: Callable[[Optional[ServiceInfo]], None]
    ) -> None:
        super().__init__()
        self.finishedHandler = finishedHandler

    def run(self) -> None:
        zeroconf = Zeroconf()
        serviceinfo = zeroconf.get_service_info(
            "_streamberry._tcp.local.", "Stream Berry Server._streamberry._tcp.local."
        )
        print(serviceinfo)
        self.stop()
        self.finishedHandler(serviceinfo)
