#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Project: LogFileLVP
# File: settings_view.py
# Author: Christofanis Skordas (skordasc@uchicago.edu)
# -----------------------------------------------------------------------------
# Purpose:
# This file is used for the implementation of the settings view widgets.
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

from pathlib import PurePosixPath
from gsewidgets import Label, DirectoryBrowserButton, FilePathInputBox, HorizontalLine
from qtpy.QtCore import QSize
from qtpy.QtGui import QIcon
from qtpy.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout

from logfilelvp.model import PathModel


class SettingsView(QFrame):
    """This class is responsible for displaying the settings of the LogfileLVP application."""

    def __init__(self, directories: PathModel) -> None:
        super(SettingsView, self).__init__()

        self._directories = directories

        # Widgets
        self._lbl_settings = Label("Settings", object_name="lbl-large")
        self._lbl_base_directory = Label("Base Directory", object_name="lbl-settings-first")
        self.btn_select_base_directory = DirectoryBrowserButton(
            size=QSize(38, 38), object_name="button-directory", icon=QIcon(PurePosixPath(self._directories.icon_path).joinpath("experiments.svg").as_posix())
        )
        self.input_filepath = FilePathInputBox(
            placeholder="Base directory path",
            object_name="input-directory",
            invalid_characters='<>"|?*#&$',
        )

        # Settings methods
        self.configure_settings_and_settings_widgets()
        self.configure_settings_layout()

    def configure_settings_and_settings_widgets(self) -> None:
        """Configure the settings and the settings widgets."""
        # Set the object name
        self.setObjectName("settings")

        # Set the style sheet
        self.setStyleSheet(open(PurePosixPath(self._directories.style_path).joinpath("settings.qss").as_posix(), "r").read())

    def configure_settings_layout(self) -> None:
        """Configure the settings layout."""
        # Base directory layout
        base_directory_layout = QHBoxLayout()
        base_directory_layout.setContentsMargins(0, 0, 0, 0)
        base_directory_layout.setSpacing(0)
        base_directory_layout.addWidget(self.input_filepath)
        base_directory_layout.addWidget(self.btn_select_base_directory)

        # Settings layout
        settings_layout = QVBoxLayout()
        settings_layout.setContentsMargins(0, 0, 10, 0)
        settings_layout.setSpacing(0)
        settings_layout.addWidget(self._lbl_settings)
        settings_layout.addWidget(HorizontalLine(object_name="line-settings"))
        settings_layout.addWidget(self._lbl_base_directory)
        settings_layout.addLayout(base_directory_layout)
        settings_layout.addStretch(1)

        # Set the layout
        self.setLayout(settings_layout)
