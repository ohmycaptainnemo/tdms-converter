from __future__ import annotations
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtCore import QRect
from typing import Tuple


class ProgressBar(QProgressBar):
    """ProgressBar object for showing the progress of the conversion of the tdms file."""

    def __init__(self, *args, **kwargs):
        """ProgressBar constructor. Note that the range and initial value for the progress bar are set here."""
        QProgressBar.__init__(self, *args, **kwargs)

        # For overriding the overall theme. You will then also need to import Path library.
        # self.setStyleSheet(
        #     open(Path(__file__).parent / "styles" / "classic-style.css").read()
        # )

        self.setValue(0)
        self.setRange(0, 100)

    def set_text(self, text: str) -> ProgressBar:
        """Method for setting the text of a progressbar.

        Args:
            text (str): String for the text of the progressbar.

        Returns:
            ProgressBar: ProgressBar object.
        """
        self.setText(text)
        return self

    def set_name(self, text: str) -> ProgressBar:
        """Method for setting object name.

        Args:
            text (str): object name.

        Returns:
            ProgressBar: ProgressBar object.
        """
        self.setObjectName(text)
        return self

    def set_geometry(self, geometry: Tuple[int, int, int, int]) -> ProgressBar:
        """Method for setting the position and size of a widget.

        Args:
            geometry (Tuple[int, int, int, int]): x, y, width and height of the widget respectively.

        Returns:
            ProgressBar: ProgressBar object.
        """
        self.setGeometry(QRect(*geometry))
        return self

    def set_size(self, size: Tuple[int, int]) -> ProgressBar:
        """Method for setting the size of a widget.

        Args:
            size (Tuple[int, int]): Width and height of the widget respectively.

        Returns:
            ProgressBar: ProgressBar object.
        """
        self.setFixedSize(*size)
        return self
