from tkinter import *
from tkinter import ttk

from Client.ResultsWindow import ResultsWindow

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

        # Store user-selected teams
        self.red_teams = []
        self.blue_teams = []

        self.draw()


    def draw(self):
        """
        Draws the components to the screen.

        - Title
        - Red / blue alliance team dropdowns
        - Predict button
        """

        # Title
        title = ttk.Label(self, text='Predict a match', font=('*', 26))
        title.pack()

        # Create prediction frames
        prediction_frame = ttk.Frame(self)
        prediction_frame.pack()

        self.red_alliance_frame = ttk.Frame(prediction_frame)
        self.blue_alliance_frame = ttk.Frame(prediction_frame)
        self.red_alliance_frame.pack(side=LEFT)
        self.blue_alliance_frame.pack(side=LEFT)

        # Labels for alliances
        ttk.Label(self.red_alliance_frame, text='Red alliance').pack()
        ttk.Label(self.blue_alliance_frame, text='Blue alliance').pack()

        # Add team to alliance button
        ttk.Button(self.red_alliance_frame, text='+', command=lambda: self.increase_team(self.RED)).pack()
        ttk.Button(self.blue_alliance_frame, text='+', command=lambda: self.increase_team(self.BLUE)).pack()

        # Predict button
        ttk.Button(self, text='Predict match', command=self.handle_predict_button).pack()


    def increase_team(self, alliance):
        """
        Add a team entry to the selected alliance.

        Create team number variable, and add to list.
        Reference: https://docs.python.org/3/library/tkinter.html#coupling-widget-variables

        Then, add dropdown menu to screen.

        Parameter
        ----------

        alliance
            the alliance to increase a team to
        """

        all_team_numbers = globals.Prediction.prediction.get_team_numbers()
        team_var = StringVar()

        # Sort team numbers
        try:
            all_team_numbers = sorted(all_team_numbers, key=lambda team_number: int(team_number))
        except ValueError:
            pass # Don't sort if team numbers are not numeric

        # Create dropdown menu

        if alliance == self.RED:
            self.red_teams.append(team_var)
            ttk.OptionMenu(self.red_alliance_frame, team_var, '', '', *all_team_numbers).pack()

        elif alliance == self.BLUE:
            self.blue_teams.append(team_var)
            ttk.OptionMenu(self.blue_alliance_frame, team_var, '', '', *all_team_numbers).pack()


    def handle_predict_button(self):
        """
        Handle the predict button.

        1. Process teams
        Use filter() to remove blank values, and map() to get string values.
        Lastly, use list() to convert generator to a list.

        References:
        https://docs.python.org/3/library/tkinter.html#coupling-widget-variables
        https://docs.python.org/3/howto/functional.html#generators


        2. Predict match
        Passes teams into backend, receives
        prediction data, and display to user.
        """

        # Process teams (see docstring for more info)
        red_alliance_teams = filter(lambda team_number: team_number.get(), self.red_teams)
        red_alliance_teams = map(lambda team_number: team_number.get(), red_alliance_teams)
        red_alliance_teams = list(red_alliance_teams)

        blue_alliance_teams = filter(lambda team_number: team_number.get(), self.blue_teams)
        blue_alliance_teams = map(lambda team_number: team_number.get(), blue_alliance_teams)
        blue_alliance_teams = list(blue_alliance_teams)

        # Predict match
        prediction_results = globals.Prediction.prediction.predict_match(red_alliance_teams, blue_alliance_teams)
        ResultsWindow(self.master, prediction_results)
        self.destroy()