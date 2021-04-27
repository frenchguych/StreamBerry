import sys

from typing import Dict

from PyQt5.QtCore import QCoreApplication
from streamberry.button import BaseButton


class ExitButton(BaseButton):
    def __init__(self, row: int, col: int, icon_off: str, icon_on: str, config: Dict) -> None:
        super().__init__(row, col, icon_off, icon_on)

    def handle(self) -> None:
        QCoreApplication.quit()
