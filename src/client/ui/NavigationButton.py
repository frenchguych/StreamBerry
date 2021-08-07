from enum import Enum

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QSizePolicy
from toolkit.ui.BaseButton import BaseButton


class NavigationButton(BaseButton):
    class Type(Enum):
        PREVIOUS = 1
        NEXT = 2
        UP = 3

    def __init__(self, type: Type, iconFile: str) -> None:
        super().__init__(iconFile)
        self.initComponent()

    def initComponent(self) -> None:
        self.type = type
        self.setIconSize(QSize(40, 40))
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

    def handle(self) -> None:
        print(f"Handling button {self.type}")
