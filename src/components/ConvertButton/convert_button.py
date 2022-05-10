from __future__ import annotations
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QRect, QThread
from typing import Tuple
from functools import partial

from ...modules.utils import assess_paths, Worker


class ConvertButton(QPushButton):
    """ConvertButton object for handling conversion event and triggers."""

    def __init__(self, *args, **kwargs):
        """Constructor for initialising the ConvertButton. One can also override styles here and add custom ones specifically to the ConvertButton."""
        QPushButton.__init__(self, *args, **kwargs)

        # For overriding the overall theme. You will then also need to import Path library.
        # self.setStyleSheet(
        #     open(Path(__file__).parent / "styles" / "classic-style.css").read()
        # )

        self.source_browse_element = None
        self.destination_browse_element = None
        self.message_box = None
        self.progress_bar = None
        self.status_bar = None

        self.clicked.connect(self.handle_convert_event)

    def set_text(self, text: str) -> ConvertButton:
        """Method for setting the text of a button.

        Args:
            text (str): String for the text of the button.

        Returns:
            ConvertButton: ConvertButton object.
        """
        self.setText(text)
        return self

    def set_name(self, text: str) -> ConvertButton:
        """Method for setting object name.

        Args:
            text (str): object name.

        Returns:
            ConvertButton: ConvertButton object.
        """
        self.setObjectName(text)
        return self

    def set_geometry(self, geometry: Tuple[int, int, int, int]) -> ConvertButton:
        """Method for setting the position and size of a widget.

        Args:
            geometry (Tuple[int, int, int, int]): x, y, width and height of the widget respectively.

        Returns:
           ConvertButton: ConvertButton object.
        """
        self.setGeometry(QRect(*geometry))
        return self

    def set_size(self, size: Tuple[int, int]) -> ConvertButton:
        """Method for setting the size of a widget.

        Args:
            size (Tuple[int, int]): Width and height of the widget respectively.

        Returns:
            ConvertButton: ConvertButton object.
        """
        self.setFixedSize(*size)
        return self

    def pass_down_widget(self, *widgets) -> ConvertButton:
        """Method used for accessing reference of the widgets passed down from the main program.

        Returns:
            ConvertButton: ConvertButton object.
        """
        (
            self.source_browse_element,
            self.destination_browse_element,
            self.message_box,
            self.progress_bar,
            self.status_bar,
        ) = widgets
        return self

    def track_progress(self, count: int) -> None:
        """Method for tracking the progress of the conversion and updating the progress bar.

        Args:
            count (int): Integer value of the progress.
        """
        self.progress_bar.setValue(count)
        self.status_bar.showMessage(f"Converting file... {count}%")

    def track_group(self, group_name: str) -> None:
        """For keeping a track of the group names in the tdms file during conversion.

        Args:
            group_name (str): The group name in the tdms file.
        """
        self.message_box.setText(f"Converting for group {group_name}...")

    def conversion_finished(self) -> None:
        """Method for handling when the conversion is finished."""
        self.message_box.setText("Conversion successful.")
        self.status_bar.showMessage("Conversion successful.")
        self.setEnabled(True)

    def conversion_failed(self) -> None:
        """Method for handling when the conversion has failed."""
        self.message_box.setText("Conversion failed.")
        self.status_bar.showMessage("Conversion failed.")
        self.setEnabled(True)

    def run_job(
        self, source_browse_element_text: str, destination_browse_element_text: str
    ) -> None:
        """Running a conversion job using a thread object.

        Args:
            source_browse_element_text (str): The text from the text box of the browser source element.
            destination_browse_element_text (str): The text from the text box of the browser destination element.
        """
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(
            partial(
                self.worker.tdms_convertor,
                source_browse_element_text,
                destination_browse_element_text,
            )
        )
        self.worker.conversion_finished.connect(self.thread.quit)
        self.worker.conversion_finished.connect(self.worker.deleteLater)
        self.worker.conversion_failed.connect(self.conversion_failed)
        self.worker.conversion_failed.connect(self.thread.quit)
        self.worker.conversion_failed.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.conversion_progress.connect(self.track_progress)
        self.worker.conversion_group.connect(self.track_group)
        self.thread.start()

        self.setEnabled(False)
        self.thread.finished.connect(self.conversion_finished)

    def handle_convert_event(self) -> None:
        """Handling the pressing of the convert button. Initialises a thread to do the conversion."""
        self.message_box.setText("")
        self.status_bar.showMessage("")

        source_browse_element_text = self.source_browse_element.get_textbox_text()
        destination_browse_element_text = (
            self.destination_browse_element.get_textbox_text()
        )

        message_box_text = assess_paths(
            source_browse_element_text, destination_browse_element_text
        )

        if message_box_text != "":
            self.message_box.setText(message_box_text)

        else:
            self.run_job(source_browse_element_text, destination_browse_element_text)
