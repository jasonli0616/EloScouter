from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
import traceback

import PredictScouter

from . import globals
from .ColumnWindow import ColumnWindow
from .PredictWindow import PredictWindow


class MainWindow(Tk):

    def __init__(self):
        """
        Initialize the Main Window.

        - Configures screen size
        - Configures screen title
        - Draw components to the screen
        """

        super().__init__()

        self.report_callback_exception = self.handle_errors

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

        # Title bar
        title = ttk.Label(self, text='EloScouter', font=('*', 32))
        title.pack()

        # Import CSV button
        import_button = ttk.Button(self, text='Import CSV file', command=self.handle_import_button)
        import_button.pack()

        # Help button
        help_button = ttk.Button(self, text='Help', command=self.handle_help_button)
        help_button.pack()


    def handle_errors(self, *args):
        """
        Display error messages to the user.

        ALL errors, including purposely raised errors by
        the program (eg. team doesn't exist) will be handled
        by this method.
        """

        error = traceback.format_exception(*args)

        # Gather error message
        main_error = error[-1]
        error.pop()

        error_message = 'An error has occcured:\n\n'    \
                        + f'{main_error}\n\n'           \
                        + '----- Advanced: -----\n\n'   \
                        + '\n'.join(error)

        messagebox.showerror('Error', error_message, parent=self.focus_get())


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

            # Display column selection window
            # Hide main window, re-show when selection finished
            column_select = ColumnWindow(self)
            self.withdraw()
            column_select.wait_window()
            self.deiconify()

            # If columns have been selected, move to next step
            if globals.Prediction.prediction.get_column_types():

                # Show imported file
                ttk.Label(self, text='Imported file:').pack()
                ttk.Label(self, text=csv_file_dialog.name, wraplength=self.winfo_width()).pack()

                # Show predict button
                ttk.Button(self, text='Predict a match', command=self.handle_predict_button).pack()

        else:

            # Display error on cancel
            raise FileNotFoundError('File import cancelled, no CSV file imported.')


    def handle_help_button(self):
        """
        Display the user manual to the user.

        Functionality to be implemented in a later version.
        """
        pass


    def handle_predict_button(self):
        """
        Handle the predict match button.

        This button will only be shown once the information
        from the CSV file has been collected, and a prediction
        can actually be made.
        """

        predict_window = PredictWindow(self)
        predict_window.focus()