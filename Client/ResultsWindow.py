from tkinter import *
from tkinter import ttk

import PredictScouter

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

        self.prediction_results = prediction_results

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

        # Get points and team data
        # See PredictScouter.predict_match() docstring for more info
        red_points, blue_points, red_teams, blue_teams = self.prediction_results

        # Determine winning alliance
        winning_message = 'Tie'
        if red_points > blue_points:
            winning_message = 'Red alliance wins!'
        elif blue_points > red_points:
            winning_message = 'Blue alliance wins!'

        ttk.Label(self, text=winning_message, font=('*', 30)).pack()

        # Display tables
        self.create_table(red_teams, 'Red Alliance')
        self.create_table(blue_teams, 'Blue Alliance')


    def create_table(self, team_data, title):
        """
        
        Parameters
        ----------

        team_data: list[Team]
            list of the teams data

        title: str
            the title of the table
        """

        # Display title
        ttk.Label(self, text=f'\n{title}', font=('*', 20)).pack()

        # Table
        table = ttk.Treeview(self)
        columns = list(globals.Prediction.prediction.get_column_types().keys())

        # Sanitize data
        columns.remove(PredictScouter.columns.MATCH_NUMBER)

        # Create columns
        table['columns'] = tuple(columns)

        table.column('#0', width=0, stretch=NO)
        table.heading('#0', text='', anchor=CENTER)

        # Insert column heading
        for column in columns:
            table.column(column, anchor=CENTER, stretch=NO)
            table.heading(column, text=column, anchor=CENTER)

        # Sort team list by ranking (highest to lowest)
        team_data = sorted(team_data, key=lambda team: team.ranking, reverse=True)
        
        team_index = 0

        # Insert team data
        for team in team_data:

            # Sanitize data
            team_data = team.match_column_averages
            team_data_values = list(team_data.values())
            team_data_values.insert(0, team.team_number)

            table.insert(parent='', index=team_index, iid=team_index, values=tuple(team_data_values))

            team_index += 1

        table.pack(fill='x')