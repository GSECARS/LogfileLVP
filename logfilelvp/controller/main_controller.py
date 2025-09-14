#!/usr/bin/python3
# ----------------------------------------------------------------------------------
# Project: LogfileLVP
# File: logfilelvp/controller/main_controller.py
# ----------------------------------------------------------------------------------
# Purpose:
# This file is used to control the main application for LogfileLVP.
# ----------------------------------------------------------------------------------
# Author: Christofanis Skordas
#
# Copyright (C) 2024-2025 GSECARS, The University of Chicago, USA
# ----------------------------------------------------------------------------------

from importlib.metadata import version

from wx import App

from logfilelvp.model import MainModel
from logfilelvp.view import MainView

__all__ = ["MainController"]


# Get the current version and start the GUI
try:
    __version__ = version("logfilelvp")
except Exception:
    __version__ = "unknown"


class MainController:
    """Main controller for the application."""

    def __init__(self) -> None:
        self._app = App(False)
        self._model = MainModel()
        self._view = MainView(None, title=f"LogfileLVP v.{__version__}")

        self._view.display()

    def run(self) -> None:
        """Run the main application loop."""
        self._app.MainLoop()
