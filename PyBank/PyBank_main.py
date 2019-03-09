import os
import csv

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
