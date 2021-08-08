from PyQt5.QtWidgets import QApplication

from client.ui.main_window import MainWindow


class App(QApplication):
    def __init__(self) -> None:
        super().__init__([])
        self.app = QApplication([])
        self.initComponent()
        self.initListeners()

    def initComponent(self) -> None:
        self.mainWindow = MainWindow()
        self.mainWindow.show()

    def initListeners(self) -> None:
        pass
