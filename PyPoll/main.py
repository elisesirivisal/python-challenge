import os
import csv

# variables
total_votes = 0         # total number of votes cast
charles_votes = 0       # total votes Charles Casper Stockham received
diana_votes = 0         # total votes Diana DeGette received
raymon_votes = 0        # total votes Raymon Anthony Doane received

budget_csv = os.path.join("PyPoll/Resources/election_data.csv")

with open(budget_csv) as file:
    csv_reader = csv.reader(file, delimiter = ",")
    
    # take header
    header = next(csv_reader)

    for row in csv_reader:
        total_votes += 1
        if row[2] == "Charles Casper Stockham":
            charles_votes += 1
        elif row[2] == "Diana DeGette":
            diana_votes += 1
        elif row[2] == "Raymon Anthony Doane":
            raymon_votes += 1

# find winner
if charles_votes > diana_votes and charles_votes > raymon_votes:
    winner = "Charles Casper Stockham"
elif diana_votes > charles_votes and diana_votes > raymon_votes:
    winner = "Diana DeGette"
elif raymon_votes > charles_votes and raymon_votes > diana_votes:
    winner = "Raymon Anthony Doane"

# Create "Analysis" folder in "PyBank" folder
os.mkdir("PyPoll/Analysis")
with open("PyPoll/Analysis/analysis.txt", "w") as f:
    # Write the Election Results into analysis.txt
    f.write(f"Election Results \n")
    f.write(f"-------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write(f"-------------------------\n")
    f.write(f"Charles Casper Stockham: {round((charles_votes/total_votes)*100, 3)}% ({charles_votes})\n")
    f.write(f"Diana DeGette: {round((diana_votes/total_votes)*100, 3)}% ({diana_votes})\n")
    f.write(f"Raymon Anthony Doane: {round((raymon_votes/total_votes)*100, 3)}% ({raymon_votes})\n")
    f.write(f"-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write(f"-------------------------")

with open("PyPoll/Analysis/analysis.txt", "r") as f:
    # Reads Election Results that was written in analysis.txt
    print(f.read())
# print(f"-------------------------")
