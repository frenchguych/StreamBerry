import functools
import typing
from client.network.NetworkConnectionWorker import NetworkConnectionWorker

from client.ui.Footer import Footer
from client.ui.Grid import Grid
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from toolkit.core.BaseWorker import BaseWorker
from toolkit.ui.BaseButton import BaseButton
from toolkit.ui.ButtonWorker import ButtonWorker


class MainWindow(QWidget):
    def __init__(
        self,
    ) -> None:
        self.initComponent()
        self.initListeners()
        self.initCommunications()
        self.initNetwork()

    def initComponent(self) -> None:
        super().__init__()
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

    def initCommunications(self) -> None:
        self.__worker: typing.Optional[BaseWorker] = None

    def __handleFinished(self) -> None:
        self.__worker = None

    def handleButton(self, btn: BaseButton) -> None:
        if self.__worker is None:
            self.__worker = ButtonWorker(btn, self.__handleFinished)
            self.__worker.start()

    def initNetwork(self) -> None:
        if self.__worker is None:
            self.__worker = NetworkConnectionWorker(self.__handleFinished)
            self.__worker.start()
