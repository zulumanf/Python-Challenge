
#import
import os
import csv

#telling Python where to access the csv database to read it
py_bank_csv = os.path.join('PyBank/Resources/budget_data.csv')

#initializing lists
Months_List = []
Profit_Losses_List = []
rev_change = []
max_rev_change_date = []
min_rev_change_date = []
Date = []
avg_rev_change = []

#open the file as a csv file
with open (py_bank_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    #skipping the header
    next(csv_reader)

    #for loop to store put the values from the csv to the strings that were previously defined, 
    # can make "line" be anything like row just have to change it in the appropiate code as well
    for line in csv_reader:
        Months_List.append(f"{line[0]}")
        Profit_Losses_List.append(f"{line[1]}")
        Date.append(f"{line[0]}")



#in this loop I did total of difference between all row of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change. 
    for i in range(1,len(Profit_Losses_List)):
        
        Profit_Losses_List = [ int(i) for i in Profit_Losses_List ]

        rev_change.append(Profit_Losses_List[i] - Profit_Losses_List[i-1])

        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(Date[rev_change.index(max(rev_change))+1])
        min_rev_change_date = str(Date[rev_change.index(min(rev_change))+1])
        


        
#List comprehensions - making every string number in the list an integer
Profit_Losses_List = [ int(x) for x in Profit_Losses_List ]

print("Financial Analysis")
print("----------------------------")
print('Total Months: ' + str(len(Months_List)))
print("Total:$", sum(Profit_Losses_List))
#make it only be two decimal places
print("Average Change:$", (avg_rev_change))
print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")

 #BEGINNING OF TERMINAL OUTPUT
    #Prints "Financial Analysis"
print("Financial Analysis")
    #Prints ------ to seperate title
print("----------------------------")
    #Prints total number of months 
print('Total Months: '+ str(len(Months_List)))
    #Prints Total profit/losses summed up together
Profit_Losses_List =[ int(x) for x in Profit_Losses_List]
print("Total: $", sum(Profit_Losses_List))
    #Prints Rev Changes 
print("Average Change:$", (avg_rev_change))
print("Greatest Increase in Profits: " + max_rev_change_date, max_rev_change)
print("Greastest Decrease in Profits: " + min_rev_change_date, min_rev_change)

#OUTPUT ANALYSIS TO TXT FILE IN "ANALYSIS" FOLDER
#Define Output File Path
pybank_output_path = os.path.join("PyBank", "Analysis", "pyBank_analysis.txt")
outputfile = open(pybank_output_path, "x")
outputfile.write("Financial Analysis\n")
outputfile.write("----------------------------\n")
outputfile.write("Total Months: ")
outputfile.write(str(len(Months_List)))
outputfile.write("\n")
outputfile.write("Total: $")
outputfile.write(str(sum(Profit_Losses_List)))
outputfile.write("\n")
outputfile.write("Average Change: $")
outputfile.write(str(avg_rev_change))
outputfile.write("\n")
outputfile.write("Greatest Increase in Profits: ")
outputfile.write(str(max_rev_change_date))
outputfile.write("  $")
outputfile.write(str(max_rev_change))
outputfile.write("\n")
outputfile.write("Greatest Decrease in Profits: ")
outputfile.write(str(min_rev_change_date))
outputfile.write("  $")
outputfile.write(str(min_rev_change))
outputfile.write("\n")


    



