#!/usr/bin/python3
# ----------------------------------------------------------------------------------
# Project: LogfileLVP
# File: logfilelvp/utils/shortcut.py
# ----------------------------------------------------------------------------------
# Purpose:
# This file is used to create a desktop shortcut for the LogfileLVP application.
# ----------------------------------------------------------------------------------
# Author: Christofanis Skordas
#
# Copyright (C) 2024-2025 GSECARS, The University of Chicago, USA
# ----------------------------------------------------------------------------------

import shutil

from pyshortcuts import make_shortcut

__all__ = ["create_shortcut"]


def create_shortcut() -> None:
    """Creates a desktop shortcut."""
    print("Creating desktop shortcut...")

    # Find the executable
    logfilevlp_exe = shutil.which("logfilelvp")
    if not logfilevlp_exe:
        raise FileNotFoundError("Could not find the LogfileLVP executable.")

    # Create the shortcut
    make_shortcut(f"{logfilevlp_exe} -g", name="LogfileLVP", terminal=False)
