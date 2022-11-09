import os
import csv

output_path=os.path.join("..","Resources","budget_data.csv")

file= csv.DictReader(output_path)

month=[]
profit_losses=[]
change=[]

with open(output_path,'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    
    for col in csvreader:
        month.append(col[0])
        profit_losses.append(col[1])

    profits=[int(z) for z in profit_losses]
    x=len(month)
    y=sum(profits)
    i=1
    while i<len(profit_losses):
        change.append(float(profit_losses[i])-float(profit_losses[i-1]))
        i+=1
    greatest_increase=max(change)
    greatest_decrease=min(change)
    index_decrease= change.index(greatest_decrease)
    index_increase= change.index(greatest_increase)
    print("Financial Analysis")
    print("-"*20+'\n')
    print(f'Total Months: {x}')
    print(f'Total: ${y}')
    print(f'Average Change: ${round(sum(change)/len(change),2)}')
    print(f'Greatest Increase in Profits: {month[index_increase+1]} (${round(greatest_increase)})')
    print(f'Greatest Decrease in Profits: {month[index_decrease+1]} (${round(greatest_decrease)})')
    analysis= open("PyBank_Analysis.txt", 'w')
    analysis.write("Financial Analysis"+'\n')
    analysis.write("-"*20+'\n')
    analysis.write(f'Total Months: {x}'+'\n')
    analysis.write(f'Total: ${y}'+'\n')
    analysis.write(f'Average Change: ${round(sum(change)/len(change),2)}'+'\n')
    analysis.write(f'Greatest Increase in Profits: {month[index_increase+1]} (${round(greatest_increase)})'+'\n')
    analysis.write(f'Greatest Decrease in Profits: {month[index_decrease+1]} (${round(greatest_decrease)})'+'\n')
    analysis.close()
