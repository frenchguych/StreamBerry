from enum import Enum

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QSizePolicy
from toolkit.ui.base_button import BaseButton


class NavigationButton(BaseButton):
    class Type(Enum):
        PREVIOUS = 1
        NEXT = 2
        UP = 3

    def __init__(self, btnType: Type, iconFile: str) -> None:
        super().__init__(iconFile)
        self.btnType = btnType
        self.initComponent()

    def initComponent(self) -> None:
        self.setIconSize(QSize(42, 42))
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setDisabled(True)
        self.initialized = True
