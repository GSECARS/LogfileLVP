#!/usr/bin/python3
# ----------------------------------------------------------------------------------
# Project: LogfileLVP
# File: logfilelvp/__init__.py
# ----------------------------------------------------------------------------------
# Purpose:
# This file is used to initialize the LogfileLVP package.
# ----------------------------------------------------------------------------------
# Author: Christofanis Skordas
#
# Copyright (C) 2024-2025 GSECARS, The University of Chicago, USA
# ----------------------------------------------------------------------------------

import argparse

__all__ = ["main"]

from logfilelvp.controller import start_GUI
from logfilelvp.utils import create_shortcut


def main() -> None:
    """Main entry point for the LogfileLVP application."""
    parser = argparse.ArgumentParser(description="A python application for creating experiment run folders and logs")
    parser.add_argument("-m", "--make-icon", action="store_true", help="create desktop shortcut")
    parser.add_argument("-g", "--gui", action="store_true", help="start the GUI application")

    args = parser.parse_args()

    if args.make_icon:
        # Create desktop shortcut
        create_shortcut()
    elif args.gui:
        # Start the GUI application
        start_GUI()
    else:
        # Display help message
        parser.print_help()


if __name__ == "__main__":
    main()
