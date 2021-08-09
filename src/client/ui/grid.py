from typing import List

from PyQt5.QtWidgets import (
    QGridLayout,
    QWidget,
)

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
