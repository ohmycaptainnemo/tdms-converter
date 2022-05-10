from __future__ import annotations
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import QRect
from pathlib import Path
from typing import Tuple


class HorizontalSeparator(QFrame):
    """HorizontalSeparator object for spacing/separation between components."""

    def __init__(self, *args, **kwargs):
        """Constructor for initialising the HorizontalSeparator."""
        QFrame.__init__(self, *args, **kwargs)
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)

        # For overriding the overall theme. You will then also need to import Path library.
        self.setStyleSheet(
            open(Path(__file__).parent / "styles" / "classic-style.css").read()
        )

    def set_name(self, text: str) -> HorizontalSeparator:
        """Method for setting object name.

        Args:
            text (str): object name.

        Returns:
            HorizontalSeparator: HorizontalSeparator object.
        """
        self.setObjectName(text)
        return self

    def set_geometry(self, geometry: Tuple[int, int, int, int]) -> HorizontalSeparator:
        """Method for setting the position and size of a widget.

        Args:
            geometry (Tuple[int, int, int, int]): x, y, width and height of the widget respectively.

        Returns:
           HorizontalSeparator: HorizontalSeparator object.
        """
        self.setGeometry(QRect(*geometry))
        return self

    def set_size(self, size: Tuple[int, int]) -> HorizontalSeparator:
        """Method for setting the size of a widget.

        Args:
            size (Tuple[int, int]): Width and height of the widget respectively.

        Returns:
            HorizontalSeparator: HorizontalSeparator object.
        """
        self.setFixedSize(*size)
        return self
