from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox

from click import command

import PredictScouter

from . import globals


class PredictWindow(Toplevel):

    def __init__(self, master):
        """
        Initialize the prediction window.

        - Configures screen size
        - Configures screen title
        - Draw components to the screen
        """

        super().__init__(master)

        self.title('EloScouter - Predict match')

        # Define constant variables representing
        # red and blue alliance (referenced by GUI)
        self.RED = 0
        self.BLUE = 1

        self.draw()


    def draw(self):
        """
        Draws the components to the screen.

        - Title
        - Red / blue alliance team input
        - Predict button
        """

        title = ttk.Label(self, text='Predict a match', font=('*', 26))
        title.pack()

        # Create prediction frames
        prediction_frame = ttk.Frame(self)
        prediction_frame.pack()

        self.red_alliance_frame = ttk.Frame(prediction_frame)
        self.blue_alliance_frame = ttk.Frame(prediction_frame)
        self.red_alliance_frame.pack(side=LEFT)
        self.blue_alliance_frame.pack(side=LEFT)

        ttk.Label(self.red_alliance_frame, text='Red alliance').pack()
        ttk.Label(self.blue_alliance_frame, text='Blue alliance').pack()

        ttk.Button(self.red_alliance_frame, text='+', command=lambda: self.increase_team(self.RED)).pack()
        ttk.Button(self.blue_alliance_frame, text='+', command=lambda: self.increase_team(self.BLUE)).pack()

        ttk.Button(self, text='Predict match').pack()


    def increase_team(self, alliance):
        """
        Add a team entry to the selected alliance.
        """

        if alliance == self.RED:
            ttk.Entry(self.red_alliance_frame).pack()

        elif alliance == self.BLUE:
            ttk.Entry(self.blue_alliance_frame).pack()


    def handle_predict_button(self):
        """
        Handle the predict button.

        Passes teams into backend, receives
        prediction data, and display to user.
        """