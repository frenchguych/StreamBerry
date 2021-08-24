import json
from google.protobuf import any_pb2
from common.socket_wrapper import SocketWrapper

from proto.streamberry_pb2 import ButtonInfo, GetPage
from server.config import Config


def getPage(config: Config, client: SocketWrapper, anyMessage: any_pb2.Any):
    message = GetPage()
    anyMessage.Unpack(message)
    pageName = message.page
    page = [page for page in config.pages if page.name == pageName][0]
    buttons = page.buttons
    client.sendint(len(buttons))
    for button in buttons:
        buttonInfo = ButtonInfo()
        buttonInfo.name = button.name
        buttonInfo.label = button.label
        buttonInfo.type = button.type
        buttonInfo.icon = button.icon
        buttonInfo.params = json.dumps(button.params)
        print("Check 1")
        client.send(buttonInfo.SerializeToString())
        print("Check 2")
        with open(f"{button.icon}", "rb") as buttonFile:
            buffer = buttonFile.read()
            client.send(buffer)
