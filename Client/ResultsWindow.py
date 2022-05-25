from tkinter import *
from tkinter import ttk

from . import globals


class ResultsWindow(Toplevel):

    def __init__(self, master, prediction_results):
        """
        Initialize the prediction window.

        - Configures screen size
        - Configures screen title
        - Draw components to the screen

        Parameters
        ----------

        prediction_results: tuple
            prediction results

            see PredictScouter.predict_match() docstring for more info
        """

        super().__init__(master)

        self.title('EloScouter - Match Results')

        self.draw()


    def draw(self):
        """
        Draws the components to the screen.

        - Title
        - Table displaying results
        """

        # Title
        title = ttk.Label(self, text='Results', font=('*', 26))
        title.pack()

        # TODO: Table here