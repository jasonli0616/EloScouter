from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox

import PredictScouter

from . import globals


class ColumnWindow(Toplevel):

    def __init__(self, master, column_name):
        """
        Initialize the column selection window.

        - Configures screen size
        - Configures screen title
        - Draw components to the screen

        Parameters
        ----------

        column_name
            preset column name to ask
        """

        super().__init__(master)

        self.title('EloScouter - Select columns')

        self.column_name = column_name

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

        ttk.Label(dropdowns_frame, text=f'{self.column_name}: ').pack(side=LEFT)

        all_csv_columns = globals.Prediction.prediction.get_columns()

        self.csv_column_name = StringVar()
        ttk.OptionMenu(dropdowns_frame, self.csv_column_name, '', *all_csv_columns).pack()

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

        Puts the CSV column name into the global dict variable.

        Destroys the window (main process may pop-up new window
        for next column).
        """
        csv_column_name = self.csv_column_name.get()

        if csv_column_name:
            globals.GUI.selected_columns[self.column_name] = csv_column_name

        self.destroy()