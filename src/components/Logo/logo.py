from __future__ import annotations
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect
from pathlib import Path
from typing import Tuple


class Logo(QLabel):
    """Logo object for displaying logos."""

    def __init__(self, *args, **kwargs):
        """Constructor object for the logo."""
        QLabel.__init__(self, *args, **kwargs)
        self.passed_down_widgets = None

        # For overriding the overall theme. You will then also need to import Path library.
        self.setStyleSheet(
            open(Path(__file__).parent / "styles" / "classic-style.css").read()
        )

        self.setScaledContents(True)

    def set_image(self, image_name: str) -> Logo:
        """Given an image name, this method will look for that image name in the assets directory and load it onto a QPixmap.

        Args:
            image_name (str): Name of the image.

        Returns:
            Logo: Logo object.
        """
        self.image = QPixmap(
            str(Path(__file__).parent.parent.parent / "assets" / image_name)
        )
        self.setPixmap(self.image)
        return self

    def set_text(self, text: str) -> Logo:
        """Method for setting the text of a logo.

        Args:
            text (str): String for the text of the logo.

        Returns:
            Logo: Logo object.
        """
        self.setText(text)
        return self

    def set_name(self, text: str) -> Logo:
        """Method for setting object name.

        Args:
            text (str): object name.

        Returns:
            Logo: Logo object.
        """
        self.setObjectName(text)
        return self

    def set_geometry(self, geometry: Tuple[int, int, int, int]) -> Logo:
        """Method for setting the position and size of a widget.

        Args:
            geometry (Tuple[int, int, int, int]): x, y, width and height of the widget respectively.

        Returns:
           Logo: Logo object.
        """
        self.setGeometry(QRect(*geometry))
        return self

    def set_size(self, size: Tuple[int, int]) -> Logo:
        """Method for setting the size of a widget.

        Args:
            size (Tuple[int, int]): Width and height of the widget respectively.

        Returns:
            Logo: Logo object.
        """
        self.setFixedSize(*size)
        return self
