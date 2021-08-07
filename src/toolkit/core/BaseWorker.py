from typing import Callable

from PyQt5.QtCore import QObject, QThread, pyqtSignal


class BaseWorker(QObject):
    def __init__(self) -> None:

        super().__init__()

        self.__thread = QThread()
        self.moveToThread(self.__thread)
        self.__thread.started.connect(self.run)

    def start(self) -> None:
        self.__thread.start()

    def stop(self) -> None:
        self.__thread.quit()
