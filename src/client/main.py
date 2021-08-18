from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread

from client.ui import MainWindow
from client.network.network_worker import NetworkWorker


if __name__ == "__main__":

    app = QApplication([])

    network_worker = NetworkWorker()
    network_thread = QThread()
    network_worker.moveToThread(network_thread)
    network_thread.started.connect(network_worker.run)
    network_thread.start()

    mainWindow = MainWindow()
    mainWindow.show()

    app.exec()
