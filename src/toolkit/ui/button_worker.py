from typing import Callable
from toolkit.core.base_worker import BaseWorker

from toolkit.ui.base_button import BaseButton


class ButtonWorker(BaseWorker):
    def __init__(self, button: BaseButton, finishedHandler: Callable) -> None:
        super().__init__()
        self.button = button
        self.finishedHandler = finishedHandler

    def run(self) -> None:
        # Do something with the button
        if self.button.initialized:
            print(f"Do something with the button ! {self.button}")

        # Stop the worker thread
        self.stop()

        # Callback to the mainWindow
        self.finishedHandler()
