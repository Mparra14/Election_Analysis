#the data we need to retrieve
#1.the total number of votes cast
#2. A complete list of candidates who recieved the votes
#3.The percentage of votes each candidate won
#4.The total number of votes each candidate won
#5.The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os
#assign a variable for the file to load and the path
file_to_load= os.path.join("Resources","election_results.csv") 

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#set the total votes equal to zero
total_votes= 0

#candidate options
candidate_options= []

#candidate votes with an empty dictionary
candidate_votes={}
#winning candidate and winning count tracker
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the election results and read 
with open(file_to_load) as election_data:
     # To do: read and analyze the data here.
     # Read the file object with the reader function.
    file_reader= csv.reader(election_data)
    
    #read and print the header row
    headers= next(file_reader)
    print(headers)

    #  each row in the CSV file.
    for row in file_reader:
    #add to the total vote count
        total_votes += 1
    #print the candidate name for each row
        candidate_name= row[2]
    #if the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
    #add candidate name to candidate options
         candidate_options.append(candidate_name)

    #begin tracking candidate vote count, we are setting the name vote to zero
         candidate_votes[candidate_name]= 0

    #start counting the votes after setting it to zero
        candidate_votes[candidate_name]+= 1
# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

#  To do: print out the winning candidate, vote count and percentage to
print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary =(
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)
#   terminal.


#print candidate votes
#print(candidate_votes)
