import socket
from struct import unpack
from typing import List, Optional

from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon, QPixmap
from google.protobuf.any_pb2 import Any
from zeroconf import Zeroconf

from proto.streamberry_pb2 import GetPage

from client import signals


class NetworkWorker(QObject):
    def __init__(self) -> None:
        super().__init__()
        self.sock: Optional[socket.socket] = None

    def connectToServer(self) -> None:
        print("Connecting to server")
        zeroconf = Zeroconf()
        serviceinfo = zeroconf.get_service_info(
            "_streamberry._tcp.local.", "Stream Berry Server._streamberry._tcp.local."
        )

        address: str = ""
        port: int = 0

        if serviceinfo is not None:
            address = socket.inet_ntop(socket.AF_INET, serviceinfo.addresses[0])
            port = serviceinfo.port

            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((address, port))

        if self.sock is None:
            signals.responses.connectionFailed.emit()
        else:
            signals.responses.connected.emit()

    def getPage(self, page: int) -> None:
        if self.sock is None:
            print("sock is null...")
            signals.responses.pages.emit([])
        else:
            message = GetPage()
            message.page = page
            anyMessage = Any()
            anyMessage.Pack(message)  # pylint: disable=no-member
            strmsg = anyMessage.SerializeToString()
            self.sock.sendall(strmsg)

            buf = self.sock.recv(4)
            count = unpack("!i", buf)[0]
            icons: List[QIcon] = []
            for i in range(count):
                buf = self.sock.recv(4)
                size = unpack("!i", buf)[0]
                buf = self.sock.recv(size)
                pixmap = QPixmap()
                pixmap.loadFromData(buf)
                icon = QIcon(pixmap)
                icons.append(icon)
            signals.responses.pages.emit(icons)

    def run(self) -> None:
        signals.requests.connect.connect(self.connectToServer)
        signals.requests.get_page.connect(self.getPage)
