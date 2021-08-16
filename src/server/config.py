from os import environ, path
from typing import Any

import yaml


def readConfig() -> Any:
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

    print(pages)

    return config
