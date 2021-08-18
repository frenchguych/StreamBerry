from socket import socket
from struct import pack, unpack
from typing import Tuple
from google.protobuf import any_pb2

from google.protobuf.message import Message


class SocketWrapper:
    def __init__(self, sock: socket) -> None:
        self.sock = sock

    def listen(self, backlog: int) -> None:
        self.sock.listen(backlog)

    def getsockname(self) -> Tuple[str, int]:
        return self.sock.getsockname()

    def accept(self) -> Tuple["SocketWrapper", Tuple[str, int]]:
        (client, addr) = self.sock.accept()
        return (SocketWrapper(client), addr)

    def __enter__(self) -> "SocketWrapper":
        return self

    def __exit__(self, excType, excValue, traceback) -> None:
        self.sock.close()

    def send(self, buffer: bytes) -> None:
        size = pack("!i", len(buffer))
        self.sock.send(size)
        self.sock.send(buffer)

    def sendint(self, value: int) -> None:
        buffer = pack("!i", value)
        self.sock.send(buffer)

    def sendMessage(self, message: Message) -> None:
        anyMessage = any_pb2.Any()
        anyMessage.Pack(message)
        strmsg = anyMessage.SerializeToString()
        self.send(strmsg)

    def recv(self) -> bytes:
        size = self.recvint()
        buffer = self.sock.recv(size)
        return buffer

    def recvint(self) -> int:
        buffer = self.sock.recv(4)
        value = unpack("!i", buffer)[0]
        return value

    def recvmessage(self) -> any_pb2.Any:
        buffer = self.recv()
        anyMessage = any_pb2.Any()
        anyMessage.ParseFromString(buffer)
        return anyMessage
