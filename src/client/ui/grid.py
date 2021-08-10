from typing import List

from PyQt5.QtWidgets import (
    QGridLayout,
    QLayoutItem,
    QWidget,
)

from PyQt5.QtGui import QIcon

from client.ui.grid_button import GridButton
from toolkit.ui.base_button import BaseButton


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

    def setIcons(self, icons: List[QIcon]) -> None:
        buttons: List[GridButton] = [
            self.layout().itemAt(i).widget()
            for i in range(self.layout().count())
            if isinstance(self.layout().itemAt(i).widget(), GridButton)
        ]

        for button in buttons:
            button.setIcon(QIcon("assets/button_empty.png"))
            button.setDisabled(True)

        for i in range(min(len(buttons), len(icons))):
            button = buttons[i]
            button.setIcon(icons[i])
            button.setStyleSheet("border: 0;")
            button.setDisabled(False)
