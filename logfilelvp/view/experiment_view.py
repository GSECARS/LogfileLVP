#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Project: LogFileLVP
# File: experiment_view.py
# Author: Christofanis Skordas (skordasc@uchicago.edu)
# -----------------------------------------------------------------------------
# Purpose:
# This file is used for the implementation of the experiment view widgets.
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


class ExperimentView(QFrame):
    """This class is responsible for displaying the experiment view of the LogfileLVP application."""

    def __init__(self, directories: PathModel) -> None:
        super(ExperimentView, self).__init__()

        self._directories = directories

        # Widgets
        self._lbl_experiment = Label("Experiment", object_name="lbl-large")

        # Configure the experiment view
        self.configure_experiment_view_and_view_widgets()
        self.configure_experiment_view_layout()

    def configure_experiment_view_and_view_widgets(self) -> None:
        """Configure the experiment view and the experiment view widgets."""
        # Set the object name
        self.setObjectName("experiment")

        # Set the style sheet
        self.setStyleSheet(open(PurePosixPath(self._directories.style_path).joinpath("experiment.qss").as_posix(), "r").read())

    def configure_experiment_view_layout(self) -> None:
        """Configure the layout of the experiment view."""
        # Experiment layout
        experiment_layout = QVBoxLayout()
        experiment_layout.setContentsMargins(0, 0, 0, 0)
        experiment_layout.setSpacing(0)
        experiment_layout.addWidget(self._lbl_experiment)
        experiment_layout.addWidget(HorizontalLine(object_name="line-settings"))
        experiment_layout.addStretch(1)

        # Set the layout
        self.setLayout(experiment_layout)
