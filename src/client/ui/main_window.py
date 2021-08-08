import functools
import typing

from PyQt5.QtWidgets import QVBoxLayout, QWidget
from zeroconf import ServiceInfo

from client.network.network_connection_worker import NetworkConnectionWorker
from client.ui.footer import Footer
from client.ui.grid import Grid
from toolkit.core.base_worker import BaseWorker
from toolkit.ui.base_button import BaseButton
from toolkit.ui.button_worker import ButtonWorker


class MainWindow(QWidget):
    def __init__(
        self,
    ) -> None:
        super().__init__()
        self.worker: typing.Optional[BaseWorker] = None
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

    def handleFinished(self) -> None:
        self.worker = None

    def handleButton(self, btn: BaseButton) -> None:
        if self.worker is None:
            self.worker = ButtonWorker(btn, self.handleFinished)
            self.worker.start()

    def initNetwork(self) -> None:
        def handleFinished(serviceInfo: typing.Optional[ServiceInfo]) -> None:
            if serviceInfo is None:
                self.footer.setStatus("Cannot connect to server")
            else:
                self.footer.setStatus("Connected.")
                self.footer.enableButtons()
                self.grid.enableButtons()

        if self.worker is None:
            self.worker = NetworkConnectionWorker(handleFinished)
            self.worker.start()