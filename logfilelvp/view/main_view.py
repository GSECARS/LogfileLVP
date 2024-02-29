#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Project: LogfileLVP
# File: main_view.py
# -----------------------------------------------------------------------------
# Purpose:
# This file is used to create the main application view for the project.
# -----------------------------------------------------------------------------
# Author: Christofanis Skordas
#
# Copyright (C) 2024 GSECARS, The University of Chicago, USA
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.#
# -----------------------------------------------------------------------------

from qtpy.QtWidgets import QMainWindow


class MainView(QMainWindow):
    """This class is responsible for creating the main application view for LogfileLVP."""

    def __init__(self) -> None:
        """Initializes the main application view for LogfileLVP."""
        super(MainView, self).__init__()

    def display_window(self, version: str) -> None:
        """Displays the main application window."""
        # Set the window title based on the version of the application
        self.setWindowTitle(f"LogfileLVP {version}")
        # Display the main application window
        self.showNormal()
