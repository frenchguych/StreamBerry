from typing import Optional
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QSizePolicy
from client.signals import requests

from client.toolkit.ui.base_button import BaseButton
from proto.streamberry_pb2 import ButtonInfo


class GridButton(BaseButton):

    buttonInfo: Optional[ButtonInfo]

    def __init__(self) -> None:
        super().__init__("assets/button_empty.png")
        self.initComponent()
        self.buttonInfo = None

    def initComponent(self) -> None:
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setIconSize(QSize(150, 130))
        self.setDisabled(True)
        self.pressed.connect(self.handlePressed)
        self.released.connect(self.handleReleased)

    def handlePressed(self) -> None:
        self.setIconSize(QSize(148, 128))
        if self.buttonInfo is not None:
            requests.handle_button.emit(self.buttonInfo)

    def handleReleased(self) -> None:
        self.setIconSize(QSize(150, 130))
