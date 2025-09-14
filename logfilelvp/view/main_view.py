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

from wx import Frame


class MainView(Frame):
    """Main view for the application."""

    def __init__(self, parent, title) -> None:
        super(MainView, self).__init__(parent, title=title)

    def display(self) -> None:
        """Display the main view."""
        self.Show()
