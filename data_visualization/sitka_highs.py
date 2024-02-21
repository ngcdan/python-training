import csv

import matplotlib.pyplot as plt
from datetime import datetime


first_date = datetime.strptime('2024-02-20', '%Y-%m-%d')
print(first_date)

filename = 'data_visualization/data/sitka_weather_07-2014.csv'

with open(filename) as f:
    reader = csv.reader(f) # Create reader object associate that file
    header_row = next(reader) # return next line in the file, the first line is the header row

    # The enumerate func return both index and value of each item in the list.
    for index, header_name in enumerate(header_row):
        print(index, header_name)

    # reader has row remaining exclude the header
    # Get high temperature from this file
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)

    # Plot the high temperatures
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    fig.autofmt_xdate()

    # Format plot
    plt.title('Daily high temperatures', fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()







