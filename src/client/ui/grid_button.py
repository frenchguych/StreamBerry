from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QSizePolicy

from client.toolkit.ui.base_button import BaseButton


class GridButton(BaseButton):
    def __init__(self) -> None:
        super().__init__("assets/button_empty.png")
        self.initComponent()

    def initComponent(self) -> None:
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setIconSize(QSize(150, 130))
        self.setDisabled(True)
        self.pressed.connect(self.handlePressed)
        self.released.connect(self.handleReleased)

    def handlePressed(self) -> None:
        print("Handle pressed")
        self.setIconSize(QSize(148, 128))

    def handleReleased(self) -> None:
        print("Handle released")
        self.setIconSize(QSize(150, 130))
