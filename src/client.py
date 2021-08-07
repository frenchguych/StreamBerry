import os
import socket
from functools import partial
from logging import setLoggerClass

import zeroconf
from google.protobuf.any_pb2 import Any
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QIconEngine, QPixmap
from PyQt5.QtWidgets import (QApplication, QGridLayout, QHBoxLayout,
                             QHeaderView, QLabel, QPushButton, QSizeGrip,
                             QSizePolicy, QWidget)
from zeroconf import Zeroconf

from proto.streamberry_pb2 import Ping, Pong
from ui.client.App import StreamBerryApp


def clickbtn(btn: QPushButton, checked: bool) -> None:
    print(f"Button {btn} clicked, checked is {checked} !")
    row = btn.property("row")
    column = btn.property("column")
    print(f"Row {row}, column: {column}")

if "__main__" == __name__:
    #zeroconf = Zeroconf()
    #serviceinfo = zeroconf.get_service_info(
    #    '_streamberry._tcp.local.',
    #    'Stream Berry Server._streamberry._tcp.local.connect.
    #    any.Pack(ping)connect.
    #    data = any.SerializeToString()
    #    sock.sendalapp = QApplication([])l(data)

    app = StreamBerryApp()
    app.exec()
