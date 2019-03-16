import os
import csv

candidatedict = {}
total_votes = 0
path = os.path.join("election_data.csv")

with open(path,newline="") as data:
    data_reader = csv.reader(data,delimiter=',')
    data_header = next(data_reader)

    for row in data_reader:
        total_votes += 1
        if row[2] not in candidatedict:
            candidatedict[row[2]] = 0
        candidatedict[row[2]] += 1 


print("Total Votes: " + str(total_votes))
print("-------------------------------------------------")

with open("Election Results.txt", 'w') as f:
    f.write(f"Total Votes:  {str(total_votes)}\n")
    f.write("-------------------------------------------------\n") 

    for key,value in candidatedict.items():   
        print(key, "  ", str(round((value/total_votes)*100,2)),"%  ", value)  
        f.write(f"{key}  {round((value/total_votes)*100,2)}%  {value}\n")
    print("-------------------------------------------------")
    print("Winner :", str(max(candidatedict, key=candidatedict.get)))
    f.write("-------------------------------------------------\n")
    f.write(f"Winner :{max(candidatedict, key=candidatedict.get)}\n")