import yaml
import time
import os.path

from streamberry.button import BaseButton, ButtonWorker
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QSizePolicy, QWidget

from streamberry.page import Page, PageBuilder
from typing import Dict, List


class StreamBerryEngine:

    def __init__(self) -> None:
        self.__pages: Dict[str, Page] = {}
        self.__grid = [[None for col in range(5)] for row in range(3)]
        self.__thread: QtCore.QThread = None
        self.__worker: ButtonWorker = None

    def init(self, config_file: str) -> None:
        """
        Initialize the engine:
           - Reads the config file
           - Builds the necessary structures
           - Checks if index page is present
        """
        if not config_file:
            raise RuntimeError("Argument config_file cannot be null")

        with open(config_file, "r") as stream:
            config = yaml.safe_load(stream)

        self.dirname = os.path.dirname(config_file)

        if not 'pages' in config:
            raise RuntimeError("Invalid config file : node 'pages' not found")

        for config_page in config['pages']:
            page = PageBuilder.build(config_page, self.dirname)
            self.__pages[config_page['name']] = page

        if not "index" in self.__pages:
            raise RuntimeError("Invalid config file : index page not found")

    def build_grid(self) -> None:
        for row in range(3):
            for col in range(5):
                btn = QPushButton(QIcon(os.path.join(self.dirname, "empty_160.png")), None)
                btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                btn.setIconSize(QtCore.QSize(160, 160))
                btn.clicked.connect(self.handle(row, col))
                self.layout.addWidget(btn, row, col)

    def handle(self, row: int, col: int):
        def __finish_handle() -> None:
            target: BaseButton = self.__grid[row][col]
            btn: QPushButton = self.layout.itemAtPosition(
                row, col).widget()
            time.sleep(.1)
            btn.setIcon(QIcon(target.icon_off))
            self.__thread = None
            self.__worker = None

        def __handle():
            target: BaseButton = self.__grid[row][col]
            if target and not self.__thread:
                btn: QPushButton = self.layout.itemAtPosition(
                    row, col).widget()
                btn.setIcon(QIcon(target.icon_on))
                self.__thread = QtCore.QThread()
                self.__worker = ButtonWorker(target)
                self.__worker.moveToThread(self.__thread)

                self.__thread.started.connect(self.__worker.run)
                self.__worker.finished.connect(self.__thread.quit)
                self.__worker.finished.connect(self.__worker.deleteLater)
                self.__thread.finished.connect(self.__thread.deleteLater)

                self.__thread.finished.connect(__finish_handle)
                self.__thread.start()

        return __handle

    def show_page(self, page_name: str) -> None:
        if not page_name in self.__pages:
            raise RuntimeError(f"Page {page_name} does not exist")
        self.__grid = [[None for col in range(5)] for row in range(3)]
        page = self.__pages[page_name]
        for button in page.buttons:
            btn: QPushButton = self.layout.itemAtPosition(
                button.row, button.col).widget()
            btn.setIcon(QIcon(button.icon_off))
            self.__grid[button.row][button.col] = button

    def run(self) -> None:
        app = QApplication([])
        window = QWidget(flags=QtCore.Qt.FramelessWindowHint)
        window.setFixedSize(800, 480)
        self.layout = QGridLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(QtCore.QMargins(0, 0, 0, 0))

        self.build_grid()
        self.show_page("index")

        window.setLayout(self.layout)
        window.show()
        app.exec()
