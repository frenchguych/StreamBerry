from PyQt5.QtCore import QObject, pyqtSignal

from proto.streamberry_pb2 import ButtonInfo

class Requests(QObject):
    connect = pyqtSignal()
    get_page = pyqtSignal(str)
    handle_button = pyqtSignal(ButtonInfo)
