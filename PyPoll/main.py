import os
import csv
from collections import Counter


polling=os.path.join("Resources","election_data.csv")

ballot_id=[]
candidates=[]

with open(polling) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)

    for col in csvreader:
        ballot_id.append(col[0])
        candidates.append(col[2])

    votes=len(ballot_id)
    votes_per_candidate=Counter(candidates)
    largest_number_votes=max(votes_per_candidate.values())
    winner=[x for x in votes_per_candidate.keys() if votes_per_candidate[x]==largest_number_votes]
    
    total=sum(votes_per_candidate.values())
    
    report1=f"""Election Results
{"-"*20}    
Total Votes: {votes}
{"-"*20}"""  
    print(report1)
    
    for key,val in votes_per_candidate.items():
        percentages=(round(val/total*100,3))
        print(f'{key}: {percentages}% ({val})')
report2=f"""{"-"*20} 
Winner: {sorted(winner)[0]}
{"-"*20}""" 
print(report2)   

with open("PyPoll_Analysis.txt",'w') as f:
    f.write(report1+'\n')
    for key,val in votes_per_candidate.items():
        percentages=(round(val/total*100,3))
        f.write(f'{key}: {percentages}% ({val})\n')
    f.write(report2)