from typing import Callable

from PyQt5.QtCore import QObject, pyqtSignal
from toolkit.core.BaseWorker import BaseWorker
from toolkit.ui.BaseButton import BaseButton


class ButtonWorker(BaseWorker):
    def __init__(self, button: BaseButton, finishedHandler: Callable) -> None:
        super().__init__()
        self.button = button
        self.finishedHandler = finishedHandler

    def run(self) -> None:
        self.button.handle()
        self.stop()
        self.finishedHandler()
