from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton


class BaseButton(QPushButton):
    def __init__(self, iconFile: str) -> None:
        super().__init__(QIcon(iconFile), "")
        self.initialized = False
