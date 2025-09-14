# -----------------------------------------------------------------------------
#!/usr/bin/python3
# ----------------------------------------------------------------------------------
# Project: LogfileLVP
# File: logfilelvp/model/main_model.py
# ----------------------------------------------------------------------------------
# Purpose:
# This file is used to create the main application model for the project.
# ----------------------------------------------------------------------------------
# Author: Christofanis Skordas
#
# Copyright (C) 2024-2025 GSECARS, The University of Chicago, USA
# ----------------------------------------------------------------------------------

from dataclasses import dataclass, field

from logfilelvp.model.experiment_model import ExperimentModel
from logfilelvp.model.settings_model import SettingsModel

__all__ = ["MainModel"]


@dataclass
class MainModel:
    """This class is responsible for the main model for LogFileLVP."""

    _settings: SettingsModel = field(repr=False, compare=False)
    _experiments: ExperimentModel = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        self._settings = SettingsModel()
        self._experiments = ExperimentModel(experiment_settings=self.settings.experiment_settings)

    @property
    def settings(self) -> SettingsModel:
        """This property returns the settings model instance of the main model."""
        return self._settings

    @property
    def experiments(self) -> ExperimentModel:
        """This property returns the experiments model instance of the main model."""
        return self._experiments
