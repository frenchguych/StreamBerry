import functools
import typing

from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QWidget
from ui.client.Footer import Footer
from ui.client.Grid import Grid
from ui.toolkit.BaseButton import BaseButton
from ui.toolkit.ButtonWorker import ButtonWorker


class MainWindow(QWidget):
    def __init__(
        self,
    ) -> None:
        self.initComponent()
        self.initListeners()
        self.initCommunications()

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
            btn.clicked.connect(functools.partial(self.__handleButton, btn))

    def initCommunications(self) -> None:
        self.__thread: typing.Optional[QThread] = None
        self.__worker: typing.Optional[ButtonWorker] = None

    def __handleButton(self, btn: BaseButton) -> None:
        def __handleFinished() -> None:
            self.__thread = None
            self.__worker = None

        if self.__thread is None:
            self.__thread = QThread()
            self.__worker = ButtonWorker(btn)
            self.__worker.moveToThread(self.__thread)

            self.__thread.started.connect(self.__worker.run)
            self.__worker.finished.connect(self.__thread.quit)

            self.__thread.finished.connect(self.__thread.deleteLater)
            self.__worker.finished.connect(self.__worker.deleteLater)

            self.__thread.finished.connect(__handleFinished)
            self.__thread.start()
