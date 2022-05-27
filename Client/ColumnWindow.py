from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox

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
            ttk.OptionMenu(column_frame, self.column_vars[column], '', *all_csv_columns).pack(side=LEFT)

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

        # Enforce team number and match number selection
        
        if not PredictScouter.columns.TEAM_NUMBER in column_vars_filtered.keys():
            raise AttributeError('No team number selected.')
        
        elif not PredictScouter.columns.MATCH_NUMBER in column_vars_filtered.keys():
            raise AttributeError('No match number selected.')

        else:

            try:
                globals.Prediction.prediction.set_column_types(column_vars_filtered)

                self.destroy()

            except TypeError:
                globals.Prediction.prediction.clear_column_types()
                raise TypeError('Non-numeric data in CSV file.')