"""
Our team's match results are recorded in a collection of strings.
Each match is represented by a string in the format 
"x:y", where x is our team's score and y is our opponents score.
For example: ["3:1", "2:2", "0:1", ...]
"""

points_game = ["1:0","2:0","3:0","4:0","2:1","1:3","1:4","2:3","2:4","3:4"]
points_game1 = ["1:0","2:0","3:0","4:4","2:2","3:3","1:4","2:3","2:4","3:4"]


def points(games: list) -> str:
    points = 0
    for point in games:
        if point[0] > point[-1]:
            points += 3
        elif point[0] < point[-1]:
            points += 0
        else:
            points += 1 

    return points

print(points(points_game1))

