

import os
import csv

# Path to collect data from the Downloads folder
election_data = os.path.join("Downloads", "election_data.csv")

# Set variables for each value 
total_votes = 0
candidate = ""
votes_per_candidate = {}
votes_percent ={}
winner_votes = 0
winner = ""

# Read CSV file
with open(election_data,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    # Calculate vote counts
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in votes_per_candidate:
            votes_per_candidate[candidate] = votes_per_candidate[candidate] + 1
        else:
            votes_per_candidate[candidate] = 1

# Find winner
for person, vote_count in votes_per_candidate.items():
    votes_percent[person] = '{0:.0%}'.format(vote_count / total_votes)
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = person

# print out results
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
for person, vote_count in votes_per_candidate.items():
    print(f"{person}: {votes_percent[person]} ({vote_count})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")
                   
# Path to write txt file to Downloads folder
text_path = os.path.join("Downloads", "election_results.txt")
with open(text_path, "w") as text_file:
     text_file.write(
              f"Election Results\n"
              f"----------------------------\n"
              f"Total Votes: {total_votes}}\n"
              for person, vote_count in votes_per_candidate.items():
                  f"{person}: {votes_percent[person]} ({vote_count})")
              f"----------------------------\n"
              f"Winner: {winner}\n"
              f"----------------------------\n")
             
               
    
            
             
