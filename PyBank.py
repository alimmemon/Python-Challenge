
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os, csv


csvpath = os.path.join("budget_data.csv")

date_tracker = []
profit_tracker = []
change_rate = []

with open(csvpath) as csvfile: #Wrapper not sure what it means 🤦‍♂️
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # Read each row of data after the header
    for row in csvreader:
        date_tracker.append(row[0])
        profit_tracker.append(int(row[1]))
    for i in range (len(profit_tracker)-1):
        change_rate.append(profit_tracker[i+1] - profit_tracker[i])
    
    great_profit = max(change_rate)
    great_loss = min(change_rate)
    great_profit_date = change_rate.index(great_profit) + 1
    great_loss_date = change_rate.index(great_loss) + 1

financial_analysis = (f"""
    Financial Analysis
    ------------------
    Total Months = {len(date_tracker)}
    Total = ${sum(profit_tracker)}
    Average change_rate = ${round(sum(change_rate)/len(change_rate),2)}
    Greatest Increase in Profits: ${great_profit} on {date_tracker[great_profit_date]}
    Greatest Losses: ${great_loss} on {date_tracker[great_loss_date]}
""")
print(financial_analysis)

output_file = ("financial_analysis_output.txt")
with open(output_file, "w") as file:
    file.write(financial_analysis)



with open(csvpath) as csvfile: #Wrapper not sure what it means 🤦‍♂️
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # Read each row of data after the header
