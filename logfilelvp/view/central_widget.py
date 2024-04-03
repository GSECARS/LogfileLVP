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
# ----------------------------------------------------------------------

from qtpy.QtWidgets import QFrame, QGridLayout


class CentralWidget(QFrame):
    """This class is responsible for displaying the central widget for LogfileLVP."""

    def __init__(self) -> None:
        super(CentralWidget, self).__init__()

        layout = QGridLayout()
        self.setLayout(layout)
