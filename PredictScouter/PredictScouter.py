import os

class PredictScouter:

    def __init__(self, csv_file_path):
        """
        Constructor for the prediction model.

        Sets the CSV value for the 
        """

        if not os.path.isfile(csv_file_path):
            raise FileNotFoundError(f"The selected path: '{csv_file_path}' is not a file.")

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



    def set_column(self, column_type, column_name):
        """
        Set one column in the CSV file to a
        pre-determined column (in columns.py).

        Use set_columns(args) to set multiple columns.

        Parameters
        ----------

        column_type: str
            type of column

        column_name: str
            CSV column name

        example: {
            "Auto balls scored high": "balls scored high auto"
        }
        """

        self.column_types[column_type] = column_name


    def set_columns(self, columns_types: dict):
        """
        Set each column in the CSV file to a
        pre-determined columns (in columns.py).

        Use set_column(args) to set one column.

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