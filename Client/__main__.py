"""
EloScouter client

This module is the frontend client to access EloScouter.
The functionality end is located in the PredictScouter folder.

This file runs the main process.
"""

from . import globals
from .MainWindow import MainWindow

# Display the current view
window = MainWindow()


window.mainloop()