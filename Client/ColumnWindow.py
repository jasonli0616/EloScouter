from tkinter import *
from tkinter import ttk

import os
import json

import PredictScouter

from . import globals


class ColumnWindow(Toplevel):

    def __init__(self, master):
        """
        Initialize the column selection window.

        - Configures screen size
        - Configures screen title
        - Draw components to the screen
        """

        super().__init__(master)

        self.title('EloScouter - Select columns')

        # Attempt to collect files from stored cache
        # If there is not stored cache, store cache after selection
        self.cache_file_path = f'{globals.Prediction.prediction.get_csv_file_path()}.elocache'

        if os.path.isfile(self.cache_file_path):
            with open(self.cache_file_path, 'r') as f:
                data = json.load(f)
            self.set_column_types(data)

        self.draw()


    def draw(self):
        """
        Draws the components to the screen.

        - Title
        - Dropdowns to select columns
        - Next button
        """

        title = ttk.Label(self, text='Select columns', font=('*', 26))
        title.pack()

        # Create columns & dropdowns

        dropdowns_frame = ttk.Frame(self)
        dropdowns_frame.pack(expand=True)

        all_csv_columns = globals.Prediction.prediction.get_columns()
        self.column_vars = {column: StringVar() for column in PredictScouter.columns.columns}

        # Create dropdown menus
        for column in PredictScouter.columns.columns:
            column_frame = ttk.Frame(dropdowns_frame)
            column_frame.pack()
            ttk.Label(column_frame, text=f'{column}: ').pack(side=LEFT)

            # Set column default (if stored in cache)
            column_default = ''
            try:
                column_default = globals.Prediction.prediction.get_column_types()[column]
            except KeyError:
                pass # If not stored in cache

            ttk.OptionMenu(column_frame, self.column_vars[column], column_default, '', *all_csv_columns).pack(side=LEFT)

        # Next button
        next_button = ttk.Button(self, text='Submit', command=self.handle_next_button)
        next_button.pack()

        # Bind enter key press to next button
        # (lambda function is used to prevent passing
        # any arguments into self.handle_next_button())
        self.bind('<Return>', lambda x: self.handle_next_button())


    def handle_next_button(self):
        """
        Handle the submit button.

        Puts the CSV column names into the predictor.

        Destroys the window.
        """

        column_vars_filtered = dict()

        for k, v in self.column_vars.items():
            if v.get():
                column_vars_filtered[k] = v.get()

        self.set_column_types(column_vars_filtered)
        self.destroy()


    def set_column_types(self, data):
        """
        Send the CSV column names into the predictor.

        Parameters
        ----------

        data: dict
            the types of each column

            key: type of column
            value: CSV column name

            example: {
                "Auto balls scored high": "balls scored high auto"
            }
        """

        # Enforce team number and match number selection
        
        if PredictScouter.columns.TEAM_NUMBER not in data.keys():
            raise AttributeError('No team number selected.')
        
        elif PredictScouter.columns.MATCH_NUMBER not in data.keys():
            raise AttributeError('No match number selected.')

        else:

            try:

                # Store column cache (auto-fill next time)

                with open(self.cache_file_path, 'w') as f:
                    json.dump(data, f)

                # Set columns to predictor
                globals.Prediction.prediction.set_column_types(data)

            except TypeError:
                globals.Prediction.prediction.clear_column_types()
                raise TypeError('Non-numeric data in CSV file.')