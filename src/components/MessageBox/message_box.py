from __future__ import annotations
from PyQt5.QtWidgets import QLabel, QFrame
from PyQt5.QtCore import QRect, Qt
from typing import Tuple
from pathlib import Path


class MessageBox(QLabel):
    """MessageBox object for showing the messages and prompts to the user."""

    def __init__(self, *args, **kwargs):
        """Constructor initialisation for MessageBox."""
        QLabel.__init__(self, *args, **kwargs)

        # For overriding the overall theme. You will then also need to import Path library.
        self.setStyleSheet(
            open(Path(__file__).parent / "styles" / "classic-style.css").read()
        )

        self.setAlignment(Qt.AlignTop)
        self.setFixedHeight
        self.setWordWrap(True)
        self.setFrameShape(QFrame.Box)

    def set_text(self, text: str) -> MessageBox:
        """Method for setting the text of a message box.

        Args:
            text (str): String for the text of the message box.

        Returns:
            MessageBox: MessageBox object.
        """
        self.setText(text)
        return self

    def set_name(self, text: str) -> MessageBox:
        """Method for setting object name.

        Args:
            text (str): object name.

        Returns:
            MessageBox: MessageBox object.
        """
        self.setObjectName(text)
        return self

    def set_geometry(self, geometry: Tuple[int, int, int, int]) -> MessageBox:
        """Method for setting the position and size of a widget.

        Args:
            geometry (Tuple[int, int, int, int]): x, y, width and height of the widget respectively.

        Returns:
           MessageBox: MessageBox object.
        """
        self.setGeometry(QRect(*geometry))
        return self

    def set_size(self, size: Tuple[int, int]) -> MessageBox:
        """Method for setting the size of a widget.

        Args:
            size (Tuple[int, int]): Width and height of the widget respectively.

        Returns:
            MessageBox: MessageBox object.
        """
        self.setFixedSize(*size)
        return self
