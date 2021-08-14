from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread

from client.ui import MainWindow
from client.network import NetworkWorker


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


if __name__ == "__main__":

    network_worker = NetworkWorker()
    network_thread = QThread()
    network_worker.moveToThread(network_thread)
    network_thread.started.connect(network_worker.run)
    network_thread.start()

    app = App()
    app.exec()
