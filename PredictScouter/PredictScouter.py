class PredictScouter:

    def __init__(self, csv_file_path):
        """
        Constructor for the prediction model.

        Sets the CSV value for the 
        """

        self._csv_file_path = csv_file_path
        self.column_types = dict()


    def get_csv_file_path(self):
        """
        Return the path of the CSV file.
        
        Returns
        ----------

        str
            path of the CSV file
        """

        return self._csv_file_path


    def _read_csv(self) -> str:
        """
        Return the text contents of the CSV file.

        Returns
        ----------

        str
            the contents of the CSV file
        """

        with open(self._csv_file_path, 'r') as f:
            csv_contents = f.read()
            f.close()
        return csv_contents


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

        return self._read_csv()         \
                    .splitlines()[0]    \
                    .split(',')


    def set_columns(self, columns_types: dict):
        """
        Set each column in the CSV file to a
        pre-determined columns (in columns.py).

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

        self.column_types = columns_types