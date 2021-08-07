from client.ui.NavigationButton import NavigationButton
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QSizePolicy, QWidget


class Footer(QWidget):

    navigate: pyqtSignal = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.initComponent()

    def initComponent(self) -> None:
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        statusText = QLabel()
        statusText.setText("Connecting...")
        statusText.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        layout.addWidget(statusText)

        previousPageButton = NavigationButton(
            NavigationButton.Type.PREVIOUS, "assets/left-arrow.png"
        )
        layout.addWidget(previousPageButton)

        nextPageButton = NavigationButton(
            NavigationButton.Type.NEXT, "assets/right-arrow.png"
        )
        layout.addWidget(nextPageButton)

        upButton = NavigationButton(NavigationButton.Type.UP, "assets/up-arrow.png")
        layout.addWidget(upButton)

        self.setLayout(layout)

        self.buttons = [previousPageButton, nextPageButton, upButton]
