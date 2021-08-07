from PyQt5.QtWidgets import QApplication
from ui.client.MainWindow import MainWindow


class StreamBerryApp(QApplication):
    def __init__(self) -> None:
        self.app = QApplication([])
        self.initComponent()
        self.initListeners()

    def initComponent(self) -> None:
        self.mainWindow = MainWindow()
        self.mainWindow.show()

    def initListeners(self) -> None:
        pass

    def exec(self) -> None:
        self.app.exec()
