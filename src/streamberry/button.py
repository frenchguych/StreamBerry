from PyQt5.QtCore import QObject, QSize, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton, QSizePolicy

import streamberry.buttons
import importlib
import pkgutil
import os.path
import time

from typing import Dict, List, Optional


class BaseButton():
    def __init__(self, row: int, col: int, icon_off: str, icon_on: str) -> None:
        self.icon_off = icon_off
        self.icon_on = icon_on
        self.row = row
        self.col = col

    def handle():
        """ Must be implemented by children """
        pass


class ButtonBuilder():

    __modules: List = []

    def build(page_button: Dict, dirname: str) -> BaseButton:
        if not ButtonBuilder.__modules:
            ButtonBuilder.__modules = [importlib.import_module(name) for finder, name, ispkg in pkgutil.iter_modules(
                streamberry.buttons.__path__, streamberry.buttons.__name__ + ".")]

        if 'type' not in page_button:
            raise RuntimeError(
                "Invalid config file : 'button' nodes require a 'type' attribute")
        if 'icon' not in page_button:
            raise RuntimeError(
                "Invalid config file : 'button' nodes require a 'icon' attribute")
        if 'cell' not in page_button:
            raise RuntimeError(
                "Invalid config file : 'button' nodes require a 'cell' attribute")

        icon_found = False
        base_icon = os.path.join(dirname, page_button['icon'])
        if os.path.exists(base_icon):
            icon_found = True
            icon_off = icon_on = base_icon
        elif os.path.exists(f"{base_icon}.png"):
            icon_found = True
            icon_off = icon_on = base_icon
        elif os.path.exists(f"{base_icon}_on.png") and os.path.exists(f"{base_icon}_off.png"):
            icon_found = True
            icon_off = f"{base_icon}_off.png"
            icon_on = f"{base_icon}_on.png"

        if not icon_found:
            raise RuntimeError(f"Icon {base_icon} not found")

        row, col = (*[x.strip() for x in page_button['cell'].split(',')], )
        if not row.isdigit() or not col.isdigit():
            raise RuntimeError(
                f"Cell {page_button['cell']} is not a correct 'row, col' value")

        class_name = f"{page_button['type']}Button"
        classes = [getattr(module, class_name)
                   for module in ButtonBuilder.__modules if hasattr(module, class_name)]
        if 0 == len(classes):
            raise RuntimeError(
                f"Invalid config file : button type {page_button['type']} ({class_name}) not found")
        button_class = classes[0]
        button = button_class(int(row), int(
            col), icon_off, icon_on, page_button)

        return button


class ButtonWorker(QObject):
    finished = pyqtSignal()

    def __init__(self, button: BaseButton) -> None:
        super().__init__(parent=None)
        self.button = button

    def run(self) -> None:
        self.button.handle()
        self.finished.emit()
