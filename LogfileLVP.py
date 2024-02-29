#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Project: LogfileLVP
# File: LogfileLVP.py
# -----------------------------------------------------------------------------
# Purpose:
# This is the main file of the LogfileLVP project. It is used to create a GUI
# application instance using PyQt6 libraries.
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

from logfilelvp import app, __version__


if __name__ == "main":
    app.run(version=__version__)
