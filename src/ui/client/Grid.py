from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QGridLayout, QPushButton, QSizePolicy, QStyle, QStyleOptionButton, QWidget

from ui.client.GridButton import GridButton


class Grid(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initComponent()
        self.initListeners()

    def initComponent(self) -> None:
        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        for row in range(3):
            for column in range(5):
                btn = GridButton()
                layout.addWidget(btn, row, column)

    def initListeners(self) -> None:
        pass
