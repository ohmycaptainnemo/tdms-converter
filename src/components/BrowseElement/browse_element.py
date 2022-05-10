from __future__ import annotations
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QHBoxLayout, QFileDialog
from PyQt5.QtCore import QRect
from typing import Tuple


class BrowseElement(QWidget):
    """BrowseElement class for creating a browse element object including a text editor, a button and file dialog."""

    def __init__(self, *args, **kwargs):
        """Constructor for initialising the BrowseElement. One can also override styles here and add custom ones specifically to the BrowseElement."""
        QWidget.__init__(self, *args, **kwargs)

        self.browse_button = QPushButton("Browse")
        self.browse_button.setFixedSize(80, 30)
        self.browse_button.clicked.connect(self.handle_browse_event)

        self.text_box = QLineEdit("Path to file")
        self.text_box.setFixedSize(180, 30)

        # For overriding the overall theme. You will then also need to import Path library.
        # self.setStyleSheet(
        #     open(Path(__file__).parent / "styles" / "classic-style.css").read()
        # )

        layout = QHBoxLayout()
        layout.setSpacing(10)
        layout.addWidget(self.text_box)
        layout.addWidget(self.browse_button)
        self.setLayout(layout)

    def set_name(self, text: str) -> BrowseElement:
        """Method for setting object name.

        Args:
            text (str): object name.

        Returns:
            BrowseElement: BrowseElement object.
        """
        self.setObjectName(text)
        return self

    def set_textbox_text(self, text: str) -> BrowseElement:
        """Methods for setting the text in the text editor.

        Args:
            text (str): Text to add in the text editor.

        Returns:
            BrowseElement: BrowseElement object.
        """
        self.text_box.setText(text)
        return self

    def get_textbox_text(self) -> str:
        """Method for getting text editor's text.

        Returns:
            str: Text string.
        """
        return self.text_box.text()

    def set_geometry(self, geometry: Tuple[int, int, int, int]) -> BrowseElement:
        """Method for setting the position and size of a widget.

        Args:
            geometry (Tuple[int, int, int, int]): x, y, width and height of the widget respectively.

        Returns:
            BrowseElement: BrowseElement object.
        """
        self.setGeometry(QRect(*geometry))
        return self

    def set_size(self, size: Tuple[int, int]) -> BrowseElement:
        """Method for setting the size of a widget.

        Args:
            size (Tuple[int, int]): Width and height of the widget respectively.

        Returns:
            BrowseElement: BrowseElement object.
        """
        self.setFixedSize(*size)
        return self

    def handle_browse_event(self) -> None:
        """Methods for handling a button click of the BrowseElement."""
        if self.objectName() == "source_browser":
            self.source_file_path, _ = QFileDialog.getOpenFileName(
                self,
                "Open TDMS File",
                "",
                "TDMS Files (*.tdms)",
                options=QFileDialog.DontUseNativeDialog,
            )
            self.text_box.setText(self.source_file_path)
        else:
            self.destination_directory = QFileDialog.getExistingDirectory(
                self, "Select Destination Path", options=QFileDialog.DontUseNativeDialog
            )
            self.text_box.setText(self.destination_directory)
