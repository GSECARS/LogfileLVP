#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Project: LogfileLVP
# File: settings_controller.py
# -----------------------------------------------------------------------------
# Purpose:
# This is used for controlling the settings model and view for LogFileLVP.
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

from pathlib import Path

from logfilelvp.model import MainModel
from logfilelvp.view import MainView


class SettingsController:
    """This class is responsible for controlling the settings model for LogFileLVP."""

    def __init__(self, model: MainModel, view: MainView) -> None:
        """This method initializes the experiment controller for LogFileLVP."""
        self._model = model
        self._view = view

        # Run methods
        self._display_saved_settings()
        self._connect_signals()

    def _display_saved_settings(self) -> None:
        """Displays the saved settings for the settings view"""
        self._view.widgets.settings.input_filepath.setText(self._model.settings.experiment_settings.root_directory)

    def _connect_signals(self) -> None:
        """Used for connecting signals and slots for the view widgets"""
        self._view.widgets.settings.input_filepath.returnPressed.connect(self._input_filepath_changed)
        self._view.widgets.settings.btn_select_base_directory.directory_changed.connect(self._browse_to_directory_changed)

    def _input_filepath_changed(self) -> None:
        """Validates the path specified and changes the root directory"""
        directory = self._view.widgets.settings.input_filepath.text()
        self._change_root_directory(directory=directory)

    def _browse_to_directory_changed(self) -> None:
        """Changes the input filepath and the root directory"""
        directory = self._view.widgets.settings.btn_select_base_directory.directory
        self._view.widgets.settings.input_filepath.setText(directory)
        self._change_root_directory(directory=directory)

    def _change_root_directory(self, directory: str) -> None:
        """Sets the root directory for the pattern search"""
        # Validate directory
        if not Path(directory).exists():
            return None
        # Change the root directory
        self._model.settings.experiment_settings.root_directory = directory
