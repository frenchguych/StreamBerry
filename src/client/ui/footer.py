from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLayoutItem, QSizePolicy, QWidget

from client.ui.navigation_button import NavigationButton


class Footer(QWidget):

    navigate: pyqtSignal = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.initComponent()

    def initComponent(self) -> None:
        layout = QHBoxLayout()
        layout.setContentsMargins(3, 0, 3, 0)

        self.statusText = QLabel()
        self.statusText.setText("Connecting...")
        self.statusText.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.addWidget(self.statusText)

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

    def setStatus(self, status: str) -> None:
        self.statusText.setText(status)

    def enableButtons(self) -> None:
        for i in range(self.layout().count()):
            obj: QLayoutItem = self.layout().itemAt(i)
            if isinstance(obj.widget(), NavigationButton):
                btn: NavigationButton = obj.widget()
                btn.setDisabled(False)
        