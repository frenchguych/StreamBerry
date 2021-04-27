from streamberry.button import BaseButton, ButtonBuilder
from typing import Dict, List


class Page:
    def __init__(self, buttons: List[BaseButton]) -> None:
        self.buttons = buttons


class PageBuilder:
    def build(config_page: Dict, dirname: str) -> Page:
        if 'name' not in config_page:
            raise RuntimeError(
                "Invalid config file : 'page' nodes require a 'name' attribute")
        if 'buttons' not in config_page:
            raise RuntimeError(
                "Invalid config file : 'page' nodes require a 'buttons' attribute")

        buttons: List = []
        for page_button in config_page['buttons']:
            button = ButtonBuilder.build(page_button, dirname)
            buttons.append(button)

        return Page(buttons)
