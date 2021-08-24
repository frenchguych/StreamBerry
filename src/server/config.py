from os import environ, path
from typing import Any, List

import yaml

class ButtonConfig:
    id: str
    name: str
    type: str
    icon: str
    params: str

    def __init__(self, button: Any) -> None:
        self.name = button['name']
        self.label = button['label']
        self.type = button['type']
        self.icon = button['icon']
        if 'params' in button:
            self.params = button['params']
        else:
            self.params = ''
        print(self.params)

class PageConfig:
    name: str
    buttons: List[ButtonConfig]

    def __init__(self, page: Any) -> None:
        self.name = page['name']
        self.buttons = [ButtonConfig(button) for button in page['buttons']]

class BindConfig:
    address: str = "0.0.0.0"
    port: int = 0

    def __init__(self, bind: Any) -> None:
        if bind is not None and 'address' in bind:
            self.address = bind['address']
        if bind is not None and 'port' in bind:
            self.port = bind['port']

class Config:
    bind: BindConfig
    pages: List[PageConfig]

    def __init__(self, config: Any) -> None:
        self.bind = BindConfig(config.get('bind'))
        self.pages = [PageConfig(page) for page in config['pages']]

def readConfig() -> Config:
    configFiles = [
        file
        for file in [
            "streamberry.yaml",
            f"{environ['HOME']}/.config/streamberry/streamberry.yaml",
        ]
        if path.exists(file)
    ]

    if "SNAP_USER_COMMON" in environ:
        configFile = path.join(environ["SNAP_USER_COMMON"], "streamberry.yaml")
        if path.exists(configFile):
            configFiles.append(configFile)

    if len(configFiles) == 0:
        raise FileNotFoundError("streamberry.yaml")

    with open(configFiles[0], "r") as stream:
        config = yaml.safe_load(stream)

    if config is None or "pages" not in config:
        raise KeyError("Key 'pages' not found in config file")

    root = path.dirname(configFiles[0])
    root = "./" if root == "" else root

    pages = config["pages"]

    for page in pages:
        for button in page["buttons"]:
            button["icon"] = path.join(root, button["icon"])
            if not path.exists(button["icon"]):
                raise FileNotFoundError(button["icon"])

    return Config(config)
