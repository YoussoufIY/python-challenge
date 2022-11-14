#Importing modules
import os
import csv

#Assigning Path to CSV file to read
output_path=os.path.join("Resources","budget_data.csv")

file= csv.DictReader(output_path)

#Creating Lists that will hold the different values to assess
month=[]
profit_losses=[]
change=[]

#Opening and reading CSV filw
with open(output_path,'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
#Appending lists with column values    
    for col in csvreader:
        month.append(col[0])
        profit_losses.append(col[1])
#Assigning "Total Months" variable as x 
    x=len(month)
#Assigning "Total" variable as y
    profits=[int(z) for z in profit_losses]
    y=sum(profits)
#Determining the change in profit and losses from one month to
# the next and appending the result to the change list   
    i=1
    while i<len(profit_losses):
        change.append(float(profit_losses[i])-float(profit_losses[i-1]))
        i+=1
#Finding the greatest increase and decrease by using min/max
#functions on the change list 
    greatest_increase=max(change)
    greatest_decrease=min(change)
#Finding the month associated with the greatest increase and
# decrease    
    index_decrease= change.index(greatest_decrease)
    index_increase= change.index(greatest_increase)
 #Printing the report using f string  
    report = f"""Financial Analysis
{'-'*20}
Total Months: {x}
Total: ${y}
Average Change: ${round(sum(change)/len(change),2)}
Greatest Increase in Profits: {month[index_increase+1]} (${round(greatest_increase)})
Greatest Decrease in Profits: {month[index_decrease+1]} (${round(greatest_decrease)})
    """
#Printing out results onto a text file    
    print(report)
   
    with open("PyBank_Analysis.txt", 'w') as f:
        f.write(report)
