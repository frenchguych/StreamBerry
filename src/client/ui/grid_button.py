from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QSizePolicy

from toolkit.ui.base_button import BaseButton


class GridButton(BaseButton):
    def __init__(self) -> None:
        super().__init__("assets/button_empty_off.png")
        self.initComponent()

    def initComponent(self) -> None:
        self.setStyleSheet("border: none;")
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setIconSize(QSize(150, 130))
        self.setDisabled(True)
