from PyQt5.QtCore import QObject, pyqtSignal

class Responses(QObject):
    connected = pyqtSignal()
    connectionFailed = pyqtSignal()
    pages = pyqtSignal(list) # This is really a List[Tuple[ButtonInfo, QIcon]]
    release_button = pyqtSignal()
