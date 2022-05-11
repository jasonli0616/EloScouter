# Elo Rating Algorithm


## Purpose of document

The purpose of this document is to outline my learning process of the Elo algorithm, while creating EloScouter for my final performance task.


## Basic concept

Each player starts off with 0 points. When a win occurs, the amount of points given are relative to the amount of points they already have. A player with lots of points would be given less points than a player with less points. When a player wins and gains points, the points are taken from the opponent. This ensures the point gain relativity during a win is mirrored in a loss. These points are what predict a win/loss for a player against another player.


## Sources Used
https://medium.com/purple-theory/what-is-elo-rating-c4eb7a9061e0