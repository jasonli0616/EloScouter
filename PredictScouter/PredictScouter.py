import os
import csv

from . import columns

class PredictScouter:

    def __init__(self, csv_file_path):
        """
        Constructor for the prediction model.

        This opens the CSV file, and does not close it.
        The file should be closed when the program closes
        by calling PredictScouter.close_csv_file().
        """

        if not os.path.isfile(csv_file_path):
            raise FileNotFoundError(f"The selected path: '{csv_file_path}' is not a file.")

        self._csv_file_path = csv_file_path
        self._csv_file = open(csv_file_path, 'r')
        self.column_types = dict()


    def close_csv_file(self):
        """Closes the CSV file."""
        self._csv_file.close()


    def get_csv_file_path(self):
        """
        Return the path of the CSV file.
        
        Returns
        ----------

        str
            path of the CSV file
        """

        return self._csv_file_path


    def _read_csv(self):
        """
        Return the reader of the CSV file.

        Note: The file is not closed here.

        Reference:
        https://docs.python.org/3/library/csv.html#csv.reader

        Returns
        ----------

        csv.reader
            the reader of the CSV file
        """

        return csv.reader(self._csv_file)


    def get_columns(self) -> list:
        """
        Return all the columns in the CSV file.

        Retrives the first line of the CSV file,
        and splits it into a list, at every comma.
        This will return the list of the columns.

        Returns
        
        ----------

        list
            the columns in the CSV file
        """

        # return self._read_csv()         \
        #             .splitlines()[0]    \
        #             .split(',')
        return next(self._read_csv())

    def get_teams(self) -> list:
        """
        Return all the columns in the CSV file.
        """

        team_number_csv_column = self.column_types[columns.TEAM_NUMBER]



    def set_columns(self, columns_types: dict):
        """
        Set each column in the CSV file to a
        pre-determined columns (in columns.py).

        Does not overwrite pre-existing column types,
        unless using the same name.

        Preferably every column in columns.py should
        be set to a CSV column, but this is not necessary.

        Parameters
        ----------

        columns_types: dict
            the types of each column

            key: type of column
            value: CSV column name

            example: {
                "Auto balls scored high": "balls scored high auto"
            }
        """

        for key, value in columns_types.items():
            self.column_types[key] = value

        self._rank_teams()


    def _rank_teams(self):
        """
        This is the main (private) method that implements the algorithm.

        Algorithm explanation:
        For every column in each team, the outliers will be
        removed and the average will be calculated. Based on
        the positivity/negativity of the columns (eg. balls
        scored vs balls missed), a singular numeric value will
        be calculated for each team using the average of each
        column. This numeric value will serve as the ranking
        to predict a win or loss. The averaged column data will
        serve as the predicted match data.
        """

        self.get_teams()