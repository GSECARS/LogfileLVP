#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Project: LogfileLVP
# File: main_controller.py
# -----------------------------------------------------------------------------
# Purpose:
# This file is used to create the main application controller for the project.
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

import sys
from typing import Optional

from qtpy.QtWidgets import QApplication

from logfilelvp.view import MainView


class MainController:
    """This class is responsible for controlling the main application of LogfileLVP."""

    def __init__(self) -> None:
        """Initializes the main application for LogfileLVP."""
        self._app = QApplication(sys.argv)
        self._view = MainView()

    def run(self, version: Optional[str] = "") -> None:
        """Runs the main application."""
        # Display the main view
        self._view.display_window(version=version)
        # Start the PyQt application event loop and exit the Python
        # script with the status code returned by the application
        sys.exit(self._app.exec())
