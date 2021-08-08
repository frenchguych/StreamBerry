from PyQt5.QtCore import QObject, QThread


class BaseWorker(QObject):
    def __init__(self) -> None:

        super().__init__()

        self.workerThread = QThread()
        self.moveToThread(self.workerThread)
        self.workerThread.started.connect(self.run)

    def start(self) -> None:
        self.workerThread.start()

    def stop(self) -> None:
        self.workerThread.quit()
