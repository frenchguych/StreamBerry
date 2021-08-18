import functools
from typing import List, Tuple

from PyQt5.QtWidgets import QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon

from client.ui import Footer, Grid
from client.toolkit.ui import BaseButton
from client import signals
from proto.streamberry_pb2 import ButtonInfo

class MainWindow(QWidget):
    def __init__(
        self,
    ) -> None:
        super().__init__()
        self.initComponent()
        self.initListeners()
        self.initCommunications()
        signals.requests.connect.emit()

    def initComponent(self) -> None:
        self.setFixedSize(800, 480)

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        self.setLayout(layout)


        self.grid = Grid()
        layout.addWidget(self.grid)

        self.footer = Footer()
        layout.addWidget(self.footer)

    def initListeners(self) -> None:
        for btn in self.footer.buttons:
            btn.clicked.connect(functools.partial(self.handleButton, btn))
        for btn in self.grid.buttons:
            btn.clicked.connect(functools.partial(self.handleButton, btn))

    def initCommunications(self) -> None:
        signals.responses.connected.connect(self.connectedToServer)
        signals.responses.connectionFailed.connect(self.connectionFailed)
        signals.responses.pages.connect(self.pages)

    def handleFinished(self) -> None:
        pass

    def handleButton(self, btn: BaseButton) -> None:
        pass

    def connectedToServer(self) -> None:
        self.footer.setStatus("Connected.")
        self.footer.enableButtons()
        self.grid.enableButtons()
        signals.requests.get_page.emit("index")

    def connectionFailed(self) -> None:
        self.footer.setStatus("Connection failed")

    def pages(self, buttons: List[Tuple[ButtonInfo, QIcon]]) -> None:
        self.grid.setButtons(buttons)
