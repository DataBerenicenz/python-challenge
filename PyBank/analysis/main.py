import os
import csv

file = os.path.join("..","Resources","budget_data.csv")

total_months = 0
netpnl = 0
greatamount=0
decreaseamount =0
change = 0
previousval=0
dategreat = 0
datelow = 0
total_changes=0
printlist = []

with open (file, "r",encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    
    for row in csvreader:
        total_months = total_months + 1 
        netpnl = netpnl+ int(row[1])
        change  = int(row[1])-int(previousval)
        if previousval == 0:
            change = 0
        else:    
            total_changes = total_changes + change
        if int(change) > int(greatamount):
                greatamount = change
                dategreat = row[0]
        elif int(change) < int(decreaseamount):
                decreaseamount = change
                datelow = row[0]
        previousval = row[1]
        
average = round(int(total_changes)/ (int(total_months)-1),2)

result = (f"""Financial Analysis
-----------------------------
Total Months:{total_months}
Total: ${netpnl}
Average Change: ${average}
Greatest Increase in Profits: {dategreat} (${greatamount})
Greatest Decrease in Profits: {datelow} (${decreaseamount})

""")
print(result)

printlist.append(result)

output_file ="financial_analysis.txt"
with open(output_file,"w") as nfile:
    csv_writer =csv.writer(nfile)
    
    csv_writer.writerow(printlist)
