#!/usr/bin/python3
# ----------------------------------------------------------------------------------
# Project: LogfileLVP
# File: logfilelvp/utils/settings_model.py
# ----------------------------------------------------------------------------------
# Purpose:
# This file is used to create the settings model for the project.
# ----------------------------------------------------------------------------------
# Author: Christofanis Skordas
#
# Copyright (C) 2024-2025 GSECARS, The University of Chicago, USA
# ----------------------------------------------------------------------------------

from dataclasses import dataclass, field
from pathlib import Path

from wx import Config

__all__ = ["SettingsModel"]


@dataclass
class ExperimentSettingsModel:
    settings: Config = field(repr=False, compare=False)

    _root_directory: str = field(init=False, repr=False, compare=False)
    _beamline: str = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        """Initialize the ExperimentSettingsModel."""
        self._root_directory = self.settings.Read("root_directory", "")
        self._beamline = self.settings.Read("beamline", "")

    @property
    def root_directory(self) -> str:
        """Return the root directory of the experiment."""
        return self._root_directory

    @root_directory.setter
    def root_directory(self, value: str) -> None:
        """Set the root directory of the experiment."""
        if Path(value).exists():
            self._root_directory = value
            self.settings.Write("root_directory", value)

    @property
    def beamline(self) -> str:
        """Return the beamline of the experiment."""
        return self._beamline

    @beamline.setter
    def beamline(self, value: str) -> None:
        """Set the beamline of the experiment."""
        if value in ["13-BM-D", "13-ID-C", "13-ID-D"]:
            self._beamline = value
            self.settings.Write("beamline", value)


@dataclass
class SettingsModel:
    """This class is responsible for the settings model for LogFileLVP."""

    _settings: Config = field(init=False, repr=False, compare=False)
    _experiment_settings: ExperimentSettingsModel = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        self._settings = Config("LogfileLVP")
        self._experiment_settings = ExperimentSettingsModel(settings=self._settings)

    @property
    def experiment_settings(self) -> ExperimentSettingsModel:
        """This property returns the experiment settings model instance of the settings model."""
        return self._experiment_settings
