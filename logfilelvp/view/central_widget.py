#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Project: LogFileLVP
# File: central_widget.py
# Author: Christofanis Skordas (skordasc@uchicago.edu)
# -----------------------------------------------------------------------------
# Purpose:
# This file contains the central widget for the LogfileLVP application.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------

from qtpy.QtWidgets import QFrame, QHBoxLayout, QStackedWidget
from pathlib import PurePosixPath

from logfilelvp.model import PathModel
from logfilelvp.view.sidebar_view import SidebarView


class CentralWidget(QFrame):
    """This class is responsible for displaying the central widget for LogfileLVP."""

    def __init__(self, directories: PathModel) -> None:
        super(CentralWidget, self).__init__()

        self._directories = directories

        # Sidebar
        self.sidebar = SidebarView(directories=self._directories)
        self.stacked_widget = QStackedWidget(self)

        self.configure_central_widget()
        self.configure_layout()

    def configure_central_widget(self) -> None:
        """Configure the central widget."""
        # Set the object name
        self.setObjectName("central-widget")
        # Set the style sheet
        self.setStyleSheet(open(PurePosixPath(self._directories.style_path).joinpath("main.qss").as_posix(), "r").read())

    def configure_layout(self) -> None:
        """Configure the layout of the central widget."""

        # Create tne main layout
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Add the sidebar to the layout
        layout.addWidget(self.sidebar)
        layout.addWidget(self.stacked_widget)

        # Set stretch factors
        layout.setStretch(1, 1)

        # Set the layout of the central widget
        self.setLayout(layout)
