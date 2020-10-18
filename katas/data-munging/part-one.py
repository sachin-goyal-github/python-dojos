"""
# http://codekata.com/kata/kata04-data-munging/

Part One: Weather Data
In weather.dat you’ll find daily weather data for Morristown, NJ for June 2002.
Download this text file, then write a program to output the day number (column one)
with the smallest temperature spread (the maximum temperature is the second column,
the minimum the third column).
"""

lines = []
dayWithSmallestSpread = None

spread_days = {}

with open('weather.dat', 'r') as f:
    for line in f:
        columns = [column.strip() for column in line.split(' ') if column != '']
        if len(columns) >= 3 and columns[0].isnumeric():
            day = columns[0]
            spread = int(columns[1].strip("*")) - int(columns[2].strip("*"))
            spread_days[spread] = day

print(spread_days[min(spread_days.keys())])
