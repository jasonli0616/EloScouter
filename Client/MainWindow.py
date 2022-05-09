from tkinter import *
from tkinter import ttk

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
        pass


    def handle_help_button(self):
        pass