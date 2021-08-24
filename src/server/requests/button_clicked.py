from google.protobuf import any_pb2
from common.socket_wrapper import SocketWrapper
from proto.streamberry_pb2 import ButtonClicked, ClickAck
from server.config import Config


def buttonClicked(_: Config, client: SocketWrapper, anyMessage: any_pb2.Any) -> None:
    message = ButtonClicked()
    message.ParseFromString(anyMessage.value)
    print(f"Received a click request for {message.buttonInfo.name}")
    print(message.buttonInfo.params)
    # Do something with the button click
    # For example, send a message to the client
    response = ClickAck()
    client.sendMessage(response)
