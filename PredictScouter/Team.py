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
        """

        self.team_number = team_number
        self.matches = []
        self.match_column_averages = dict()
        self.ranking = 0
        self.set_team_matches_from_csv(csv_dict_reader, column_types)


    def set_team_matches_from_csv(self, csv_dict_reader, column_types):
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
            the types of each CSV column
        """

        for column in csv_dict_reader:
            column_team_number = column[column_types[columns.TEAM_NUMBER]]
            if column_team_number == self.team_number:
                self.matches.append(column)

        self.process_matches(column_types)


    def process_matches(self, column_types):
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
            the types of each CSV column
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

                # Positive / negative influence on team ranking (-1 or 1)
                column_influence = columns.columns[column_type]


    def __eq__(self, __o: object) -> bool:
        """
        Return whether an object is the same as this object.

        Check whether the object is Team, and whether the
        team number is the same.
        """

        if isinstance(__o, self.__class__):
            return __o.team_number == self.team_number

        return False