#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Project: LogFileLVP
# File: plotting_view.py
# Author: Christofanis Skordas (skordasc@uchicago.edu)
# -----------------------------------------------------------------------------
# Purpose:
# This file is used for the implementation of the plotting view widgets.
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

from gsewidgets import Label, HorizontalLine
from pathlib import PurePosixPath
from qtpy.QtWidgets import QFrame, QVBoxLayout

from logfilelvp.model import PathModel


class PlottingView(QFrame):
    """This class is responsible for displaying the plotting view of the LogfileLVP application."""

    def __init__(self, directories: PathModel) -> None:
        super(PlottingView, self).__init__()

        self._directories = directories

        # Widgets
        self._lbl_plotting = Label("Plotting", object_name="lbl-large")

        # Configure the plotting view
        self.configure_plotting_view_and_view_widgets()
        self.configure_plotting_view_layout()

    def configure_plotting_view_and_view_widgets(self) -> None:
        """Configure the plotting view and the plotting view widgets."""
        # Set the object name
        self.setObjectName("plotting")

        # Set the style sheet
        self.setStyleSheet(open(PurePosixPath(self._directories.style_path).joinpath("plotting.qss").as_posix(), "r").read())

    def configure_plotting_view_layout(self) -> None:
        """Configure the layout of the plotting view."""
        # Plotting layout
        plotting_layout = QVBoxLayout()
        plotting_layout.setContentsMargins(0, 0, 0, 0)
        plotting_layout.setSpacing(0)
        plotting_layout.addWidget(self._lbl_plotting)
        plotting_layout.addWidget(HorizontalLine(object_name="line-settings"))
        plotting_layout.addStretch(1)

        # Set the layout
        self.setLayout(plotting_layout)
