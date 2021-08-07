from PyQt5.QtCore import QObject, pyqtSignal

from ui.toolkit.BaseButton import BaseButton


class ButtonWorker(QObject):

    finished = pyqtSignal()

    def __init__(self, button: BaseButton) -> None:
        super().__init__()
        self.button = button

    def run(self) -> None:
        self.button.handle()
        self.finished.emit()
