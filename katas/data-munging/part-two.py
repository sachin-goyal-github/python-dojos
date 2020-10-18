"""
http://codekata.com/kata/kata04-data-munging/
Part Two: Soccer League Table
The file football.dat contains the results from the English Premier League for 2001/2.
The columns labeled ‘F’ and ‘A’ contain the total number of goals scored for and against each team
in that season (so Arsenal scored 79 goals against opponents, and had 36 goals scored against them).
Write a program to print the name of the team with the smallest difference in ‘for’ and ‘against’
goals.
"""

small_score_diff = None
team_name_small_score_diff = None

with open('football.dat', 'r') as results_file:
    for line in results_file:
        columns = [column.strip() for column in line.strip().split(' ') if column.strip() is not '']

        if len(columns) is 10:
            score_diff = abs(int(columns[6]) - int(columns[8]))
            if small_score_diff is None or small_score_diff > score_diff:
                small_score_diff = score_diff
                team_name_small_score_diff = columns[1]

print(team_name_small_score_diff)
