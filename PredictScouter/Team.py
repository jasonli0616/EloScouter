import csv

from . import columns

class Team:
    """
    Class for PredictScouter to represent a team.
    This is what will be used to calculate averages
    and team ranking.
    """

    def __init__(self, team_number: str):
        """
        Initialize the team.

        Parameters
        ---------

        team_number: str
            the team number (stored as a string for compatibility)
        """

        self.team_number = team_number
        self.matches = []
        self.set_team_matches_from_csv


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
            if column[column_types[columns.TEAM_NUMBER]] == self.team_number:
                self.matches.append(column)


    def __eq__(self, __o: object) -> bool:
        """
        Return whether an object is the same as this object.

        Check whether the object is Team, and whether the
        team number is the same.
        """

        if isinstance(__o, self.__class__):
            return __o.team_number == self.team_number

        return False