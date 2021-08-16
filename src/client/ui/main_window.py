import functools
from typing import Optional, List

from PyQt5.QtWidgets import QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon

from client.ui import Footer, Grid
from client.toolkit.core import BaseWorker
from client.toolkit.ui import BaseButton, ButtonWorker
from client import signals

class MainWindow(QWidget):
    def __init__(
        self,
    ) -> None:
        super().__init__()
        self.worker: Optional[BaseWorker] = None
        self.initComponent()
        self.initListeners()
        self.initCommunications()
        self.initNetwork()

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
        self.worker = None
        signals.responses.connected.connect(self.connectedToServer)
        signals.responses.connectionFailed.connect(self.connectionFailed)
        signals.responses.pages.connect(self.pages)

    def handleFinished(self) -> None:
        self.worker = None

    def handleButton(self, btn: BaseButton) -> None:
        if self.worker is None:
            self.worker = ButtonWorker(btn, self.handleFinished)
            self.worker.start()

    @staticmethod
    def initNetwork() -> None:
        signals.requests.connect.emit()

    def connectedToServer(self) -> None:
        self.footer.setStatus("Connected.")
        self.footer.enableButtons()
        self.grid.enableButtons()
        signals.requests.get_page.emit(0)

    def connectionFailed(self) -> None:
        self.footer.setStatus("Connection failed")

    def pages(self, icons: List[QIcon]) -> None:
        self.grid.setIcons(icons)
