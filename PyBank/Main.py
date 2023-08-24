
#Assignment 3 - PyBank analysis

#%%

#Import necessary modules
import os
import csv
import statistics

#Path to folder containing csv
budget_data = os.path.join(r"./Resources/budget_data.csv")

#Define variables
Dates = []
Net_Profit = 0
Profit = []

#Open the file 
with open(budget_data) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    #Set the first line as header
    header = next(csvreader)

    #Start loop to calculate values 
    for row in csvreader:
        Dates.append(row[0]) 
        Profit.append(int(row[1]))
        #Calculate net total amount over entire period
        Net_Profit = sum(Profit)

#Find total number of months included in the dataset
MonthsTotal = len(Dates)

#Calculate the total change by subtracting the first profit value from the last one
TotalChange = Profit[-1] - Profit[0]
#Use the above value to calculate and round the average to two decimals
Average = round(TotalChange / (MonthsTotal - 1), 2)


#Calculate the greated increase and decrease in profits
Changes = [Profit[i + 1] - Profit[i] for i in range(len(Profit) - 1)]
GreatestIncrease = max(Changes)
GreatestDecrease = min(Changes)

IncreaseIndex = Changes.index(GreatestIncrease)
DecreaseIndex = Changes.index(GreatestDecrease)

IncreaseDate = Dates[IncreaseIndex + 1]
DecreaseDate = Dates[DecreaseIndex + 1]

print("Financial Analysis")
print("-------------------")
print("Total Months: ", MonthsTotal)
print("Total: ", "$", Net_Profit)
print("Average Change", "$",Average)
print("Greatest Increase in Profits:", IncreaseDate, "($", GreatestIncrease,")")
print("Greatest Decrease in Profits:", DecreaseDate, "($", GreatestDecrease,")")

#Printing results as a text file
#Using triple quotes to allow multiple lines to be printed within one command
textprint = f"""Financial Analysis
-----------------------
Total Months: {MonthsTotal} 
Total: $ {Net_Profit}
Average Change: $ {Average}
Greatest Increase in Profits: {IncreaseDate} (${GreatestIncrease})
Greatest Decrease in Profits: {DecreaseDate} (${GreatestDecrease})"""

#print(textprint)

with open("PyBank.txt", "w") as f:
    f.write(textprint)
    f.close 


   
# %%

