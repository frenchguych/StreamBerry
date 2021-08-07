from PyQt5.QtWidgets import QPushButton, QSizePolicy


class GridButton(QPushButton):
    def __init__(self) -> None:
        super().__init__()
        self.initComponent()

    def initComponent(self) -> None:
        self.initialized = False
        self.setStyleSheet("border: none;")
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.clicked.connect(self.__handleClicked)

    def __handleClicked(self) -> None:
        if self.initialized:
            print("bou")
