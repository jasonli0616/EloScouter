#-----------------------------------------------------------------------------
# Name:        EloScouter Client
# Purpose:     The frontend client to access the EloScouter algorithm.
#              More information to be included with final external submission (03-June-2022).
#
# Author:      Jason Li
# Created:     05-May-2022
# Updated:     01-June-2022
#-----------------------------------------------------------------------------



from . import globals
from .MainWindow import MainWindow

# Display the current view
window = MainWindow()


window.mainloop()