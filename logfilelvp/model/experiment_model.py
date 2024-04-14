#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Project: LogFileLVP
# File: experiment_model.py
# Author: Christofanis Skordas (skordasc@uchicago.edu)
# -----------------------------------------------------------------------------
# Purpose:
# This file is used to find the next available experiment number and create
# the new experiment directory.
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

import re
from dataclasses import dataclass, field
from pathlib import Path

from logfilelvp.model.settings.experiment_settings_model import ExperimentSettingsModel


@dataclass
class ExperimentModel:
    """This class is responsible for the experiment model for LogFileLVP."""

    experiment_settings: ExperimentSettingsModel = field(repr=False, compare=False)

    _root_directory_is_invalid: bool = field(init=False, repr=False, compare=False, default=True)
    _next_experiment_number: int = field(init=False, repr=False, compare=False, default=1)

    def find_next_available_number(self) -> None:
        """Find the next available experiment number."""

        # Check if the root directory is set
        if self.experiment_settings.root_directory is None:
            self._root_directory_is_invalid = True
            return None

        # Find the next available number
        self._root_directory_is_invalid = False
        next_number = 1
        pattern = re.compile(r"[DRTP][0-9]+")

        for directory in Path(self.experiment_settings.root_directory).rglob("*"):
            # Check if it is a directory
            if directory.is_dir():

                # Check if the directory name matches the pattern
                directory_name = directory.name
                if pattern.match(directory_name):
                    number = int(re.findall(r"\d+", directory_name)[0])
                    next_number = max(next_number, number)

        self._next_experiment_number = next_number + 1

    @property
    def root_directory_is_invalid(self) -> bool:
        """Return the invalid state of the experiment directory check."""
        return self._root_directory_is_invalid

    @property
    def next_experiment_number(self) -> int:
        """Return the next experiment number."""
        return self._next_experiment_number
