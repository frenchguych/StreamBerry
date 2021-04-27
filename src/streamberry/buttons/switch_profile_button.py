from typing import Dict
from streamberry.button import BaseButton

class SwitchProfileButton(BaseButton):
    def __init__(self, row: int, col: int, icon_off: str, icon_on: str, config: Dict) -> None:
        super().__init__(row, col, icon_off, icon_on)

    def handle(self) -> None:
        pass