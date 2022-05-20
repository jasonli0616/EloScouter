# All the compatible columns in the CSV file.
# Can be changed at any time to support new competitions.

# 'Team number' and 'match number' should not be changed.

# This is stored as a dict to represent the
# positivity/negativity of the column (whether this
# data positively or negatively influences the robot).

# -2 = worse
# -1 = negative
# 0 = neutral
# 1 = positive
# 2 = better
columns = {
    'Team number': 0,
    'Match number': 0,

    # Below can be edited:
    'Auto balls scored high': 2,
    'Auto balls scored low': 1,
    'Auto balls missed high': -1,
    'Auto balls missed low': -2,
    'Tele-op balls scored high': 2,
    'Tele-op balls scored low': 1,
    'Tele-op balls missed high': -2,
    'Tele-op balls missed low': -1,
    'Climb level': 1
}

# Set a constant to represent the team & match number in the list.
TEAM_NUMBER = 'Team number'
MATCH_NUMBER = 'Match number'