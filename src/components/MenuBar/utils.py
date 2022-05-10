from pathlib import Path
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from typing import Tuple


def change_theme(
    theme: str, main_window: QMainWindow, widgets: Tuple[QWidget, ...]
) -> None:
    """Function for changing themes. Currently the logos theme needs to be
    changed using a different method compared to the rest of the app.
    The rest of the app just switches between stylesheets.

    Args:
        theme (str): Name of the string. i.e. dark or classic.
        main_window (QMainWindow): Reference to the main window object.
        widgets (Tuple[QWidget, ...]): A tuple containing the widgets for which the stylesheets need to be switched.
    """
    (
        tdms_logo,
        message_box,
    ) = widgets

    if theme == "dark":
        mask = tdms_logo.image.createMaskFromColor(QColor("black"), Qt.MaskOutColor)
        tdms_logo.image.fill(QColor("red"))
        tdms_logo.image.setMask(mask)
        tdms_logo.setPixmap(tdms_logo.image)
    else:
        mask = tdms_logo.image.createMaskFromColor(QColor("red"), Qt.MaskOutColor)
        tdms_logo.image.fill(QColor("black"))
        tdms_logo.image.setMask(mask)
        tdms_logo.setPixmap(tdms_logo.image)

    main_window.setStyleSheet(
        open(
            Path(__file__).parent.parent
            / "MainWindow"
            / "styles"
            / f"{theme}-style.css"
        ).read()
    )

    message_box.setStyleSheet(
        open(
            Path(__file__).parent.parent
            / "MessageBox"
            / "styles"
            / f"{theme}-style.css"
        ).read()
    )
