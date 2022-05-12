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

def closing_event():
    globals.Prediction.prediction.close_csv_file()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", closing_event)

window.mainloop()