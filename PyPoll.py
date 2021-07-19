import datetime as dt
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

total_vote = 0

candidate_option = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    header = next(file_reader)

    # print each row
    for row in file_reader:
        total_vote += 1
        candidate_name = row[2]
        if candidate_name not in candidate_option:
            candidate_option.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

# encoding = "utf-8" to prevent error in the code

with open(file_to_save, "w", encoding="utf-8") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_vote:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)

    for candidate_name in candidate_votes:

        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes)/float(total_vote) * 100

        candidate_results = (
            f'{candidate_name}：{vote_percentage:.1f}% ({votes:,})\n')

        print(candidate_results)

        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes
            winning_percentage = vote_percentage

            winning_candidate = candidate_name

    Winning_candidate_summary = (
        f'---------------------------\n'
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")
    print(Winning_candidate_summary)

    txt_file.write(Winning_candidate_summary)
