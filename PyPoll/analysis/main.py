import os
import csv

file = os.path.join("..","Resources","election_data.csv")

printlist = []
candidates_list= []
candidates_votes = []
total_voters = 0
votes0 = 0 
votes1 = 0
votes2 = 0
votes3 = 0
perc0 = 0
perc1 = 0
perc2 = 0
perc3 = 0
winner = ""
maxvotes = 0

with open (file, "r",encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    
    for row in csvreader:
        total_voters += 1
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
        if row[2] == candidates_list[0]:
            votes0 += 1
        elif row[2] == candidates_list[1]:
            votes1 += 1 
        elif row[2] == candidates_list[2]:
            votes2 += 1 
        elif row[2] == candidates_list[3]:
            votes3 += 1     

perc0 = round((votes0 /total_voters)*100,3)
perc1 = round((votes1 /total_voters)*100,3)
perc2 = round((votes2 /total_voters)*100,3)
perc3 = round((votes3 /total_voters)*100,3)

candidates_votes.append(votes0)
candidates_votes.append(votes1)
candidates_votes.append(votes2)
candidates_votes.append(votes3)

for x in candidates_votes:
    if candidates_votes[0] > maxvotes:
        maxvotes = candidates_votes[0]
        winner = candidates_list[0]

result = (f"""Election Results
-------------------------------
Total Votes: {total_voters}
-------------------------------
{candidates_list[0]}: {perc0}%  ({votes0})
{candidates_list[1]}: {perc1}%  ({votes1})
{candidates_list[2]}: {perc2}%  ({votes2})
{candidates_list[3]}: {perc3}%  ({votes3})
-------------------------------
Winner:{winner}
-------------------------------
""")

print(result)

printlist.append(result)

output_file ="Election_Results.txt"
with open(output_file,"w") as newfile:
    csv_writer =csv.writer(newfile)
    
    csv_writer.writerow(printlist)
    