import os
import csv

# variables
total_months = 0        # total number of months included in the dataset
total_dollar = 0        # net total amount of profits and losses
change_vals = []        # list of changes in "Profit/Losses"
max_increase = ["", 0]  # greatest INCREASE in profits (date and amount)
max_decrease = ["", 0]  # greatest DECREASE in profits (date and amount)

budget_csv = os.path.join("PyBank/Resources/budget_data.csv")

with open(budget_csv) as file:
    csv_reader = csv.reader(file, delimiter = ",")
    
    # take header
    header = next(csv_reader)

    # initialize a starting input to calculate change in profit/loss between months
    # (initializing first so we don't have to deal with checking to see if there's a next value or not)
    row = next(csv_reader)
    date = row[0]
    profit_loss = int(row[1])
    total_dollar += profit_loss
    total_months += 1

    for row in csv_reader:
        # calculate change in profit_loss between months (this month - last month)
        change_vals.append(int(row[1]) - profit_loss) # do this first before we change profit_loss to the next value

        # separating date and profit/loss, then setting respective variables to these values
        date = row[0]
        profit_loss = int(row[1])
        total_months += 1
        total_dollar += int(profit_loss)
        
        # find max INCREASE
        if max_increase[1] < change_vals[total_months - 2]:
            max_increase[0] = row[0]
            max_increase[1] = change_vals[total_months - 2]

        # find max DECREASE
        if max_decrease[1] > change_vals[total_months - 2]:
            max_decrease[0] = row[0]
            max_decrease[1] = change_vals[total_months - 2]

# calculate the average change in profit/loss over the entire period
avg_change = round(sum(change_vals)/total_months, 2)

# Create "Analysis" folder in "PyBank" folder
os.mkdir("PyBank/Analysis")
with open("PyBank/Analysis/analysis.txt", "w") as f:
    # Write the Financial Analysis into analysis.txt
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write("Total Months: " + str(total_months) + "\n")
    f.write("Total: $" + str(total_dollar) + "\n")
    f.write("Average Change: $" + str(avg_change) + "\n")
    f.write("Greatest Increase in Profits: " + str(max_increase[0]) + " ($" + str(max_increase[1]) + ")\n")
    f.write("Greatest Decrease in Profits: " + str(max_decrease[0]) + " ($" + str(max_decrease[1]) + ")")

with open("PyBank/Analysis/analysis.txt", "r") as f:
    # Reads Financial Analysis that was written in analysis.txt
    print(f.read())
