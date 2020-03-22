import os, csv
from collections import Counter

csvpath = os.path.join("election_data.csv")

with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    final_results = []
    candidate_votes = Counter(row[2] for row in csv_reader)
    total_votes = sum(candidate_votes.values())
    winner = max(candidate_votes, key=lambda key: candidate_votes[key])
    for key in candidate_votes:
        x = f"{key}: {round((candidate_votes[key] / total_votes) * 100)}% ({candidate_votes[key]})"
        final_results.append(x)
        
election_results = (f"""
    Election Results
    ------------------
    Total Votes = {total_votes}
    ------------------
    {final_results}
    ------------------
    Winner: {winner}
""")
print(election_results)

output_file = ("election_results_summary_output.txt")
with open(output_file, "w") as file:
   file.write(election_results)