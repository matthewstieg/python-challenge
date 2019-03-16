import os
import csv

print("Financial Analysis")

print('-----------------------------------------------------------------------------------')

with open('budget_data.csv') as data:
    data_reader = csv.reader(data)
    
    next(data_reader)
    months = []
    profits = []
    pdelta = []

    for row in data_reader:
        months.append(row[0])
        profits.append(int(row[1]))
    print('Total Months: ',len(months))
    print("Total: $", sum(profits))

    for i in range(1,len(profits)):
        pdelta.append(profits[i] - profits[i-1])
        avgpdelta = (sum(pdelta) / len(pdelta))
        maxpdelta = max(pdelta)
        maxpdelta_month = str(months[pdelta.index(max(pdelta))])
        minpdelta = min(pdelta)
        minpdelta_month = str(months[pdelta.index(max(pdelta))])
    print('Average Change: $', (round(avgpdelta,2)))
    print('Greatest Increase in Profits: ',maxpdelta_month,' ($',maxpdelta,')')
    print('Greatest Decrease in Profits: ',minpdelta_month,' ($',minpdelta,')')

output_file = "Financial Analysis.txt"
with open(output_file, 'w') as f:
    f.write('Financial Analysis' + '\n')
    f.write('-----------------------------------------------------------------------------------''\n')
    f.write('Total Months: ' + str(len(months)) + '\n')
    f.write("Total: $" + str(sum(profits)) + '\n')
    f.write('Average Change: $' + str((round(avgpdelta,2))) + '\n')
    f.write('Greatest Increase in Profits: ' + str(maxpdelta_month) + ' ($' + str(maxpdelta) + ')' + '\n')
    f.write('Greatest Decrease in Profits: ' + str(minpdelta_month) + ' ($' + str(minpdelta) + ')' + '\n')

