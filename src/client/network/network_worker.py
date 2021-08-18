import socket
from typing import List, Optional, Tuple

from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon, QPixmap
from google.protobuf.any_pb2 import Any
from zeroconf import Zeroconf

from proto.streamberry_pb2 import ButtonInfo, GetPage

from client import signals
from common import SocketWrapper

class NetworkWorker(QObject):
    def __init__(self) -> None:
        super().__init__()
        self.sock: Optional[SocketWrapper] = None

    def connectToServer(self) -> None:
        print("Connecting to server")
        zeroconf = Zeroconf()
        serviceinfo = zeroconf.get_service_info(
            "_streamberry._tcp.local.", "Stream Berry Server._streamberry._tcp.local."
        )

        address: str = ""
        port: int = 0

        server: Optional[socket.socket] = None
        if serviceinfo is not None:
            address = socket.inet_ntop(socket.AF_INET, serviceinfo.addresses[0])
            port = serviceinfo.port

            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.connect((address, port))

        if server is None:
            signals.responses.connectionFailed.emit()
        else:
            self.sock = SocketWrapper(server)
            signals.responses.connected.emit()

    def getPage(self, page: str) -> None:
        if self.sock is None:
            print("sock is null...")
            signals.responses.pages.emit([])
        else:
            message = GetPage()
            message.page = page
            anyMessage = Any()
            anyMessage.Pack(message)  # pylint: disable=no-member
            strmsg = anyMessage.SerializeToString()
            self.sock.send(strmsg)

            count = self.sock.recvint()
            icons: List[Tuple[ButtonInfo, QIcon]] = []
            for _ in range(count):
                buf = self.sock.recv()
                buttonInfo = ButtonInfo()
                buttonInfo.ParseFromString(buf)
                buf = self.sock.recv()
                pixmap = QPixmap()
                pixmap.loadFromData(buf)
                icon = QIcon(pixmap)
                icons.append((buttonInfo, icon))
            signals.responses.pages.emit(icons)

    def run(self) -> None:
        signals.requests.connect.connect(self.connectToServer)
        signals.requests.get_page.connect(self.getPage)
