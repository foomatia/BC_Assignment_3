
#Assignment 3 - PyPoll analysis

#%%

#Import necessary modules
import os
import csv

# Assign csv file
load = os.path.join(r"./Resources/election_data_1.csv")

# Define variables
candidate_vote = {}
winner = ""
winner_votes = 0
total_votes = -1

# Read file 
with open(load, 'r') as csvfile:
    load = csv.reader(csvfile, delimiter=",")
    header = next(load)


# PART I: Calculate the total votes and candidate votes
    
    for row in load:
        total_votes += 1


        candidates_name = row[2]
        if candidates_name  not in candidate_vote:
            candidate_vote[candidates_name] = 0
        candidate_vote[candidates_name] += 1

    print("Election Results")
    print("---------------------")
    print("Total votes: ", total_votes)
    print("---------------------")
    
# PART II: Calculate and print candidate results 
   
    for candidate_name, votes in candidate_vote.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate_name}: {percentage: .3f}% ({votes})")
        
# PART III: Identify the candidate with the highest number of votes

    for candidates_name, votes in candidate_vote.items():
        if votes > winner_votes:
            winner_votes = votes
            winner = candidates_name

    print("---------------------")
    print(f"Winner: {winner}")
    print("---------------------")  

#Printing results as a text file
#Using triple quotes to allow multiple lines to be printed within one command
    textprint = f"""Election Results
--------------------------
Total Votes: {total_votes} 
---------------------------\n"""
    for candidate_name, votes in candidate_vote.items():
        percentage = (votes / total_votes) * 100
        textprint += f"{candidate_name}: {percentage:.3f}% ({votes})\n"

    textprint += f"""---------------------------
Winner: {winner}"""

with open("PyPoll.txt", "w") as f:
    f.write(textprint)
    f.close 

# %%
