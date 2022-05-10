from __future__ import annotations
from PyQt5.QtWidgets import QMenuBar, QMenu, QAction
from PyQt5.QtCore import QRect
from typing import Tuple

from .utils import change_theme


class MenuBar(QMenuBar):
    """MenuBar object for displaying the menu bar."""

    def __init__(self, *args, **kwargs):
        """Constructor for the MenuBar object."""
        QMenuBar.__init__(self, *args, **kwargs)
        self.theme = "classic"

        self.main_window = args[0]

        self.menu_file = QMenu(self)
        self.menu_file.setObjectName("menu_file")
        self.menu_file.setTitle("&File")

        self.menu_edit = QMenu(self)
        self.menu_edit.setObjectName("menu_edit")
        self.menu_edit.setTitle("&Edit")

        self.action_close = QAction(*args, **kwargs)
        self.action_close.setObjectName("action_close")
        self.action_close.setText("&Close")
        self.action_close.triggered.connect(self.close_event)

        self.toggle_theme = QAction(*args, **kwargs)
        self.toggle_theme.setObjectName("toggle_theme")
        self.toggle_theme.setText("&Toggle Theme")
        self.toggle_theme.triggered.connect(self.toggle_theme_event)

        self.menu_file.addAction(self.action_close)
        self.menu_edit.addAction(self.toggle_theme)

        self.addAction(self.menu_file.menuAction())
        self.addAction(self.menu_edit.menuAction())

    def set_name(self, text: str) -> MenuBar:
        """Method for setting object name.

        Args:
            text (str): object name.

        Returns:
            MenuBar: MenuBar object.
        """
        self.setObjectName(text)
        return self

    def set_geometry(self, geometry: Tuple[int, int, int, int]) -> MenuBar:
        """Method for setting the position and size of a widget.

        Args:
            geometry (Tuple[int, int, int, int]): x, y, width and height of the widget respectively.

        Returns:
           MenuBar: MenuBar object.
        """
        self.setGeometry(QRect(*geometry))
        return self

    def pass_down_widget(self, *widgets) -> MenuBar:
        """Method used for accessing reference of the widgets passed down from the main program.

        Returns:
            MenuBar: MenuBar object.
        """
        self.passed_down_widgets = widgets
        return self

    def close_event(self) -> None:
        """Method for handling closing of the app and close the window."""
        self.main_window.close()

    def toggle_theme_event(self) -> None:
        """Method for handling changing of theme. Currently dark and classic theme."""

        (
            tdms_logo,
            message_box,
        ) = self.passed_down_widgets

        if self.theme == "classic":
            self.theme = "dark"
        else:
            self.theme = "classic"

        change_theme(self.theme, self.main_window, (tdms_logo, message_box))
