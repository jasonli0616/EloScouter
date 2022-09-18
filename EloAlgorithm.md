# Elo Rating Algorithm


This document outlines the algorithm used within this program.


## Basic concept

Each player starts off with 0 points. When a win occurs, the amount of points given are relative to the amount of points they already have. A player with lots of points would be given less points than a player with less points. When a player wins and gains points, the points are taken from the opponent. This ensures the point gain relativity during a win is mirrored in a loss. These points are what predict a win/loss for a player against another player.


## EloScouter implementation

The limitation of the Elo algorithm is that it only factors in wins and losses. Therefore, EloScouter will use a different algorithm with functional inspiration from Elo. For every column in each team, the outliers will be removed and the average will be calculated. Based on the positivity/negativity of the columns (eg. balls scored vs balls missed), a singular numeric value will be calculated for each team using the average of each column. This numeric value will serve as the ranking to predict a win or loss. The averaged column data will serve as the predicted match data.


## Sources Used
https://medium.com/purple-theory/what-is-elo-rating-c4eb7a9061e0