"""
EloScouter client

This module is the frontend client to access EloScouter.
The functionality end is located in the PredictScouter folder.

This file runs the main process.
"""

from . import globals
from .MainWindow import MainWindow

# Set view to homepage on first run
if not globals.GUI.view:
    globals.GUI.view = MainWindow()

# Display the current view
globals.GUI.view.mainloop()