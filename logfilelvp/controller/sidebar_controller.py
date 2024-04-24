#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Project: LogfileLVP
# File: sidebar_controller.py
# -----------------------------------------------------------------------------
# Purpose:
# This is used for controlling the sidebar behavior of the LogFileLVP
# application.
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

from typing import Optional

from logfilelvp.model import MainModel
from logfilelvp.view import MainView


class SidebarController:
    """This class is responsible for controlling the sidebar behavior of the LogfileLVP application."""

    def __init__(self, model: MainModel, view: MainView) -> None:
        """This method initializes the sidebar controller for LogfileLVP."""
        self._model = model
        self._view = view

        # Run methods
        self._connect_signals()

    def _connect_signals(self) -> None:
        """Used for connecting signals and slots for the view widgets"""
        self._view.widgets.sidebar.btn_experiments.clicked.connect(lambda: self._sidebar_button_clicked(0, experiments=True))
        self._view.widgets.sidebar.btn_plotting.clicked.connect(lambda: self._sidebar_button_clicked(1, plotting=True))
        self._view.widgets.sidebar.btn_settings.clicked.connect(lambda: self._sidebar_button_clicked(2, settings=True))

    def _sidebar_button_clicked(
        self, index: int, experiments: Optional[bool] = False, plotting: Optional[bool] = False, settings: Optional[bool] = False
    ) -> None:
        """This method is used for handling the sidebar button click."""
        self._view.widgets.stacked_widget.setCurrentIndex(index)
        self._view.widgets.sidebar.btn_experiments.setChecked(experiments)
        self._view.widgets.sidebar.btn_plotting.setChecked(plotting)
        self._view.widgets.sidebar.btn_settings.setChecked(settings)
