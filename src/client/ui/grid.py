from typing import List, Tuple

from PyQt5.QtWidgets import (
    QGridLayout,
    QLayoutItem,
    QWidget,
)

from PyQt5.QtGui import QIcon

from client.ui import GridButton
from client.toolkit.ui.base_button import BaseButton
from proto.streamberry_pb2 import ButtonInfo


class Grid(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initComponent()
        self.initListeners()

    def initComponent(self) -> None:
        layout = QGridLayout()
        layout.setContentsMargins(3, 0, 3, 0)
        self.setLayout(layout)

        self.buttons: List[BaseButton] = []

        for row in range(3):
            for column in range(5):
                btn = GridButton()
                layout.addWidget(btn, row, column)
                self.buttons.append(btn)

    def initListeners(self) -> None:
        pass

    def enableButtons(self) -> None:
        for i in range(self.layout().count()):
            obj: QLayoutItem = self.layout().itemAt(i)
            if isinstance(obj.widget(), GridButton):
                btn: GridButton = obj.widget()
                btn.setDisabled(False)

    def setButtons(self, icons: List[Tuple[ButtonInfo, QIcon]]) -> None:
        buttons: List[GridButton] = [
            self.layout().itemAt(i).widget()
            for i in range(self.layout().count())
            if isinstance(self.layout().itemAt(i).widget(), GridButton)
        ]

        for button in buttons:
            button.setIcon(QIcon("assets/button_empty.png"))
            button.setStyleSheet("")
            button.setDisabled(True)
            button.buttonInfo = None

        for i in range(min(len(buttons), len(icons))):
            button = buttons[i]
            (buttonInfo, icon) = icons[i]
            button.setIcon(icon)
            button.setStyleSheet("border: 0;")
            button.setDisabled(False)
            button.buttonInfo = buttonInfo
