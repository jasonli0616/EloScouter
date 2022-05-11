from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox

import PredictScouter

from . import globals
from .ColumnWindow import ColumnWindow


class MainWindow(Tk):

    def __init__(self):
        """
        Initialize the Main Window.

        - Configures screen size
        - Configures screen title
        - Draw components to the screen
        """

        super().__init__()

        self.geometry('300x200')
        self.title('EloScouter')

        self.draw()


    def draw(self):
        """
        Draws the components to the screen.

        - Title
        - Import CSV button
        - Help button
        """

        title = ttk.Label(self, text='EloScouter', font=('*', 32))
        title.pack()

        import_button = ttk.Button(self, text='Import CSV file', command=self.handle_import_button)
        import_button.pack()

        help_button = ttk.Button(self, text='Help', command=self.handle_help_button)
        help_button.pack()


    def handle_import_button(self):
        """
        Prompt user to import a CSV file.

        Called when import CSV button is pressed.

        If file selected:
            Set file to global variable
        If cancelled:
            Show error box
        """

        csv_file_dialog = filedialog.askopenfile(title='Select CSV file', filetypes=[('CSV file', '*.csv')])

        if csv_file_dialog:

            # Set global variables after file is imported
            globals.Prediction.csv_file = csv_file_dialog
            csv_file_dialog.close()
            globals.Prediction.prediction = PredictScouter.PredictScouter(csv_file_dialog.name)

            # Display column selection window, close current window
            for column in PredictScouter.columns:
                column_selection_window = ColumnWindow(self, column)
                column_selection_window.wait_window()

            # Set selected columns to predictor backend
            globals.Prediction.prediction.set_columns(globals.GUI.selected_columns)

            print(globals.Prediction.prediction.get_columns())

        else:

            # Display error on cancel
            messagebox.showerror('File import error', 'No CSV file imported')


    def handle_help_button(self):
        """
        Display the user manual to the user.

        Functionality to be implemented in a later version.
        """
        pass