#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Project: LogFileLVP
# File: sidebar_view.py
# Author: Christofanis Skordas (skordasc@uchicago.edu)
# -----------------------------------------------------------------------------
# Purpose:
# This file contains the SidebarView class, which is responsible for the
# sidebar of the LogFileLVP application.
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

from gsewidgets import SimpleButton
from pathlib import PurePosixPath
from qtpy.QtCore import QSize
from qtpy.QtGui import QIcon
from qtpy.QtWidgets import QFrame, QVBoxLayout

from logfilelvp.model import PathModel


class SidebarView(QFrame):
    """This class is responsible for displaying the sidebar of the LogfileLVP application."""

    def __init__(self, directories: PathModel) -> None:
        super(SidebarView, self).__init__()

        self._directories = directories

        # Sidebar buttons
        self.btn_experiments = SimpleButton(
            size=QSize(38, 38), object_name="btn-sidebar", icon=QIcon(PurePosixPath(self._directories.icon_path).joinpath("experiments.svg").as_posix())
        )
        self.btn_plotting = SimpleButton(
            size=QSize(38, 38), object_name="btn-sidebar", icon=QIcon(PurePosixPath(self._directories.icon_path).joinpath("plotting.svg").as_posix())
        )
        self.btn_settings = SimpleButton(
            size=QSize(38, 38), object_name="btn-sidebar", icon=QIcon(PurePosixPath(self._directories.icon_path).joinpath("settings.svg").as_posix())
        )

        # Sidebar methods
        self.configure_sidebar_and_widgets()
        self.configure_sidebar_layout()

    def configure_sidebar_and_widgets(self) -> None:
        """Configure the sidebar and the sidebar widgets."""
        # Set the object name
        self.setObjectName("sidebar")

        # Configure the sidebar buttons
        self.btn_experiments.setIconSize(QSize(20, 20))
        self.btn_experiments.setCheckable(True)
        self.btn_experiments.setChecked(True)
        self.btn_experiments.setChecked(True)
        self.btn_plotting.setIconSize(QSize(20, 20))
        self.btn_plotting.setCheckable(True)
        self.btn_settings.setIconSize(QSize(20, 20))
        self.btn_settings.setCheckable(True)

        # Set the stylesheet
        self.setStyleSheet(open(PurePosixPath(self._directories.style_path).joinpath("sidebar.qss").as_posix(), "r").read())

    def configure_sidebar_layout(self) -> None:
        """Configure the layout of the sidebar."""
        sidebar_layout = QVBoxLayout()
        sidebar_layout.setContentsMargins(0, 25, 0, 0)
        sidebar_layout.setSpacing(0)

        # Add the buttons to the layout
        sidebar_layout.addWidget(self.btn_experiments)
        sidebar_layout.addWidget(self.btn_plotting)
        sidebar_layout.addStretch(1)
        sidebar_layout.addWidget(self.btn_settings)

        self.setLayout(sidebar_layout)
