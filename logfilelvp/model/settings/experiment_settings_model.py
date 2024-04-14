#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Project: LogFileLVP
# File: experiment_settings_model.py
# Author: Christofanis Skordas (skordasc@uchicago.edu)
# -----------------------------------------------------------------------------
# Purpose:
# This file contains the ExperimentSettingsModel class, which is responsible for
# the settings of the experiment.
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

from dataclasses import dataclass, field
from pathlib import Path
from qtpy.QtCore import QSettings


@dataclass
class ExperimentSettingsModel:

    settings: QSettings = field(repr=False, compare=False)

    _root_directory: str | None = field(init=False, repr=False, compare=False, default=None)

    def __post_init__(self) -> None:
        """Initialize the ExperimentSettingsModel."""
        self._root_directory = self.settings.value("root_directory", type=str)

    @property
    def root_directory(self) -> str | None:
        """Return the root directory of the experiment."""
        return self._root_directory

    @root_directory.setter
    def root_directory(self, value: str) -> None:
        """Set the root directory of the experiment."""
        if Path(value).exists():
            self._root_directory = value
            self.settings.setValue("root_directory", value)
