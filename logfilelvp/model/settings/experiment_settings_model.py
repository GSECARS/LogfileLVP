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
    _beamline: str | None = field(init=False, repr=False, compare=False, default=None)

    def __post_init__(self) -> None:
        """Initialize the ExperimentSettingsModel."""
        self._root_directory = self.settings.value("root_directory", type=str)
        self._beamline = self.settings.value("beamline", type=str)

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

    @property
    def beamline(self) -> str | None:
        """Return the beamline of the experiment."""
        return self._beamline

    @beamline.setter
    def beamline(self, value: str) -> None:
        """Set the beamline of the experiment."""
        if value in ["13-BM-D", "13-ID-C", "13-ID-D"]:
            self._beamline = value
            self.settings.setValue("beamline", value)
