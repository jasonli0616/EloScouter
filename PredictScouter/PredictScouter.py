import os
import csv

from .Team import Team
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

        # Store DictReader as global variable
        # Reference: https://docs.python.org/3/library/csv.html#csv.DictReader
        with open(csv_file_path, 'r') as f:
            self._csv_dictreader = list(csv.DictReader(f))

        self._csv_file_path = csv_file_path
        self._column_types = dict()
        self.teams = []


    def get_csv_file_path(self):
        """
        Return the path of the CSV file.
        
        Returns
        ----------

        str
            path of the CSV file
        """

        return self._csv_file_path


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

        return self._csv_dictreader[0]


    def get_team_numbers(self) -> list:
        """
        Return all the columns in the CSV file.

        This method will go through all the columns in the
        CSV file, and append the team number to a list.
        The list is then converted to a set and back to a
        list, to ensure that there are no duplicates.

        Returns
        ----------

        list[str]
            a list of all the team numbers stored as a string
            (this is not a list of the Team object)
        """

        teams = []

        for column in self._csv_dictreader:

            team_number = column[self._column_types[columns.TEAM_NUMBER]].strip()
            if team_number:
                teams.append(team_number)

        return list(set(teams))


    def set_column_types(self, columns_types: dict):
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
            self._column_types[key] = value

        self._rank_teams()

    
    def clear_column_types(self):
        """
        Clear the column types.

        This is called when a non-numeric value is entered,
        and must be reset.
        """

        self._column_types = dict()


    def get_column_types(self):
        """
        Return the types of columns in the CSV file.

        See PredictScouter.set_column_types() for more info.

        Returns
        ----------

        dict
            the types of each column

            key: type of column
            value: CSV column name

            example: {
                "Auto balls scored high": "balls scored high auto"
            }
        """

        return self._column_types


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

        self.teams.clear()

        teams = self.get_team_numbers()

        for team_number in teams:
            team = Team(team_number, self._csv_dictreader, self._column_types)
            self.teams.append(team)

        self.teams = sorted(self.teams, key=lambda team: team.ranking)


    def predict_match(self, red_alliance, blue_alliance):
        """
        Predict a hypothetical match result, based on the team rankings.

        Returns match predictions as a tuple.

        Parameters
        ----------

        red_alliance: list
            list of red alliance team numbers

        blue_alliance: list
            list of blue alliance team numbers

        Returns
        ----------

        int
            total red alliance points, as determined as by algorithm

        int
            total blue alliance points, as determined as by algorithm

        list[Team]
            list of teams, sorted from highest ranking to lowest ranking
        """

        # Check that all teams are in CSV file
        for team_number in (red_alliance + blue_alliance):

            # Check that all teams are in CSV file
            all_team_numbers = list(map(lambda team: team.team_number, self.teams))
            if team_number not in all_team_numbers:
                raise KeyError(f"Team '{team_number}' not found in CSV file.")

            # Check that teams are not repeated
            if (red_alliance + blue_alliance).count(team_number) > 1:
                raise ValueError(f"Team '{team_number}' duplicated in prediction match.")

        # Get all teams in red alliance
        red_alliance_teams = list(filter(lambda team: team.team_number in red_alliance, self.teams))
        blue_alliance_teams = list(filter(lambda team: team.team_number in blue_alliance, self.teams))

        # Calculate total alliance rankings
        red_alliance_total = sum(map(lambda team: team.ranking, red_alliance_teams))
        blue_alliance_total = sum(map(lambda team: team.ranking, blue_alliance_teams))

        # List of teams ranked highest to lowest
        all_teams = sorted(red_alliance_teams + blue_alliance_teams, key=lambda team: team.ranking, reverse=True)

        return red_alliance_total, blue_alliance_total, all_teams