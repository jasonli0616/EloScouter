import numpy as np

from . import columns

class Team:
    """
    Class for PredictScouter to represent a team.
    This is what will be used to calculate averages
    and team ranking.
    """

    def __init__(self, team_number: str, csv_dict_reader, column_types):
        """
        Initialize the team.

        Parameters
        ---------

        team_number: str
            the team number (stored as a string for compatibility)

        csv_dict_reader: list[Dict]
            csv file data, structure of csv.DictReader

        column_types: dict
            the types of each column

            key: type of column
            value: CSV column name

            example: {
                "Auto balls scored high": "balls scored high auto"
            }
        """

        self.team_number = team_number
        self.matches = []
        self.match_column_averages = self._set_team_matches_from_csv(csv_dict_reader, column_types)
        self.ranking = self._set_team_ranking()


    def _set_team_matches_from_csv(self, csv_dict_reader, column_types):
        """
        Set the team matches to a class attribute.

        Loop through all scouting columns, check if it belongs
        to this team, and add to class list.

        Parameters
        ----------

        csv_dict_reader: list
            the list representation of the CSV DictReader
            https://docs.python.org/3/library/csv.html#csv.DictReader

        column_types: dict
            the types of each column

            key: type of column
            value: CSV column name

            example: {
                "Auto balls scored high": "balls scored high auto"
            }

        Returns
        ----------

        dict[str, int]
            a key-value pair of the column name, and the average
        """

        for column in csv_dict_reader:
            column_team_number = column[column_types[columns.TEAM_NUMBER]]
            if column_team_number == self.team_number:
                self.matches.append(column)

        return self._process_matches(column_types)


    def _process_matches(self, column_types):
        """
        For each column, collect all the data for this team.
        Remove the outliers, and calculate an average for that column.
        This average will be the predicted result in this column.

        Finally, (using positivity/negativity of the columns),
        calculate an overall average for this team, which will
        be the team's ranking.

        Parameters
        ----------

        column_types: dict
            the types of each column

            key: type of column
            value: CSV column name

            example: {
                "Auto balls scored high": "balls scored high auto"
            }

        Returns
        ----------

        dict[str, int]
            a key-value pair of the column name, and the average
        """

        columns_data = dict()

        for column_type, csv_column_name in column_types.items():
            if column_type not in [columns.TEAM_NUMBER, columns.MATCH_NUMBER]:

                columns_data[column_type] = []

                for match in self.matches:
                    match_data_raw = match[csv_column_name]
                    match_data = 0

                    if not match_data_raw.isnumeric() and match_data_raw:
                        raise TypeError(f"Non-numeric value '{match_data_raw}' for column '{column_type}'. Must be numeric or blank.")
                    
                    else:

                        if match_data_raw.isnumeric():
                            match_data = int(match_data_raw)

                        columns_data[column_type].append(match_data)

        for column_name, column_data in columns_data.items():

            # Remove outliers from data list, and calculate average
            column_data_no_outliers = Team.remove_outliers(column_data)
            column_average = round(sum(column_data_no_outliers) / len(column_data_no_outliers))

            columns_data[column_name] = column_average

        return columns_data


    def _set_team_ranking(self):
        """
        Create team ranking.

        The positivity/negativity of the columns (eg. balls scored vs
        balls missed), a singular numeric value will be calculated
        for each team using the average of each column.
        This numeric value will serve as the ranking to predict a win or loss.

        Returns
        ----------

        int
            the team ranking
        """

        # Start off rankings (and match amounts) at 0
        ranking_positive = 0
        ranking_positive_amount = 0

        ranking_negative = 0
        ranking_negative_amount = 0

        # Loop through columns to gather data
        for column_name, column_average in self.match_column_averages.items():
            # Get positivity/negativity of column
            column_weight = columns.columns[column_name]

            # Change ranking based on weight
            if column_weight > 0:
                ranking_positive += column_average * column_weight
                ranking_positive_amount += 1

            elif column_weight < 0:
                ranking_negative += column_average * column_weight
                ranking_negative_amount += 1

        # Divide to get average
        if (ranking_positive > 0) and (ranking_negative > 0):
            ranking_positive /= ranking_positive_amount
            ranking_negative /= ranking_negative_amount

        return round((ranking_positive - ranking_negative) * 100)


    @staticmethod
    def remove_outliers(array: list):
        """
        Remove all the outliers from an array using Numpy.

        Reference:
        https://www.adamsmith.haus/python/answers/how-to-remove-outliers-from-a-numpy-array-in-python

        Parameters
        ----------

        array: list[int]
            the array to remove outliers from

        Returns
        ----------

        list[int]
            the array with outliers removed
        """

        # Enforce array of ints
        for element in array:
            if not isinstance(element, int):
                raise TypeError(f'Can only remove outliers from list of ints.')

        np_array = np.array(array)
        np_mean = np.mean(np_array)
        np_std = np.std(np_array)

        np_dist_from_mean = abs(np_array - np_mean)
        outlier_deviation = 5
        np_not_outlier = np_dist_from_mean < outlier_deviation * np_std
        np_no_outliers = np_array[np_not_outlier]

        # If list is empty (if no outliers), return the original list
        if np_no_outliers.size == 0:
            return array

        return np_no_outliers.tolist()


    def __eq__(self, __o: object) -> bool:
        """
        Return whether an object is the same as this object.

        Check whether the object is Team, and whether the
        team number is the same.
        """

        if isinstance(__o, self.__class__):
            return __o.team_number == self.team_number

        return False