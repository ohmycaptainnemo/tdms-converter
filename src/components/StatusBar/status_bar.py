from __future__ import annotations
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtCore import QRect
from typing import Tuple


class StatusBar(QStatusBar):
    def __init__(self, *args, **kwargs):
        QStatusBar.__init__(self, *args, **kwargs)

        # For overriding the overall theme. You will then also need to import Path library.
        # self.setStyleSheet(
        #     open(Path(__file__).parent / "styles" / "classic-style.css").read()
        # )

    def set_name(self, text: str) -> StatusBar:
        """Method for setting object name.

        Args:
            text (str): object name.

        Returns:
            StatusBar: StatusBar object.
        """
        self.setObjectName(text)
        return self

    def set_geometry(self, geometry: Tuple[int, int, int, int]) -> StatusBar:
        """Method for setting the position and size of a widget.

        Args:
            geometry (Tuple[int, int, int, int]): x, y, width and height of the widget respectively.

        Returns:
            StatusBar: StatusBar object.
        """
        self.setGeometry(QRect(*geometry))
        return self
