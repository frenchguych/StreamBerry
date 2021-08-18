from PyQt5.QtCore import QObject, pyqtSignal

class Requests(QObject):
    connect = pyqtSignal()
    get_page = pyqtSignal(str)
