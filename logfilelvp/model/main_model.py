#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Project: LogfileLVP
# File: main_model.py
# -----------------------------------------------------------------------------
# Purpose:
# This file is used to create the main application model for the project.
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

from dataclasses import dataclass, field

from logfilelvp.model.settings import SettingsModel
from logfilelvp.model.path_model import PathModel
from logfilelvp.model.experiment_model import ExperimentModel


@dataclass
class MainModel:
    """This class is responsible for the main model for LogFileLVP."""

    _settings: SettingsModel = field(init=False, repr=False, compare=False)
    _directories: PathModel = field(init=False, repr=False, compare=False)
    _experiments: ExperimentModel = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        self._settings = SettingsModel()
        self._directories = PathModel()
        self._experiments = ExperimentModel(experiment_settings=self._settings.experiment_settings)

    @property
    def settings(self) -> SettingsModel:
        """This property returns the settings model instance of the main model."""
        return self._settings

    @property
    def directories(self) -> PathModel:
        """This property returns the directories model instance of the main model."""
        return self._directories

    @property
    def experiments(self) -> ExperimentModel:
        """This property returns the experiments model instance of the main model."""
        return self._experiments
