from socket import AF_INET, SOCK_STREAM, socket
from struct import unpack
from typing import List, Optional

from PyQt5.QtGui import QPixmap, QIcon


from google.protobuf.any_pb2 import Any

from proto.streamberry_pb2 import GetPage

from client.toolkit.core.base_network_connection import BaseNetworkConnection


class NetworkConnection(BaseNetworkConnection):
    def __init__(self) -> None:
        super().__init__()
        self.sock: Optional[socket] = None

    def connect(self, address: str, port: int) -> None:
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect((address, port))

    def getPage(self) -> List[QIcon]:
        print("getPage")
        if self.sock is None:
            print("sock is null...")
            return []
        message = GetPage()
        anyMessage = Any()
        anyMessage.Pack(message)  # pylint: disable=no-member
        strmsg = anyMessage.SerializeToString()
        self.sock.sendall(strmsg)
        print("Message sent")

        buf = self.sock.recv(4)
        count = unpack("!i", buf)[0]
        print(f"Count received : {count}")
        icons: List[QIcon] = []
        for i in range(count):
            print(f"Receiving button {i}")
            buf = self.sock.recv(4)
            size = unpack("!i", buf)[0]
            print(f"Size of buffer {i} : {size}")
            buf = self.sock.recv(size)
            print("Received data")
            pixmap = QPixmap()
            pixmap.loadFromData(buf)
            icon = QIcon(pixmap)
            icons.append(icon)

        return icons
    #    def worker() -> None:
    #        print("In worker")
    #        if self.workerThread is not None:
    #            print("Hello, thread !")
    #            self.workerThread.quit()
    #            self.workerThread = None
    #            print("Alles klar !")

    #    if self.workerThread is None:
    #        self.workerThread = QThread()
    #        self.moveToThread(self.workerThread)
    #        self.workerThread.started.connect(lambda: print("hello"))
    #        print("Starting thread")
    #        self.workerThread.start()
