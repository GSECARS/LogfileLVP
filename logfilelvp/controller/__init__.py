#!/usr/bin/python3
# ----------------------------------------------------------------------------------
# Project: LogfileLVP
# File: logfilelvp/controller/__init__.py
# ----------------------------------------------------------------------------------
# Purpose:
# This file is used to initialize the controller package of the LogfileLVP.
# ----------------------------------------------------------------------------------
# Author: Christofanis Skordas
#
# Copyright (C) 2024-2025 GSECARS, The University of Chicago, USA
# ----------------------------------------------------------------------------------

from logfilelvp.controller.main_controller import MainController

__all__ = ["start_GUI"]


def start_GUI() -> None:
    """Run the main application."""
    controller = MainController()
    controller.run()
