#Import Functions
import os
import csv

#telling Python where to access the csv data base to read it
py_poll_csv = os.path.join("PyPoll", "resources", "election_data.csv")

#Lists/Variables to store calculations
total_votes = []
winner = []
khan_votes = []
otooley_votes=[]
correy_votes=[]
li_votes = []

#READ INPUT FILE: budget_data.csv
#open the file as a csv file to read
with open(py_poll_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    #skip header
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")
    #Define content from csv to count for each candidate
    content = csv_file.read()
    #Counts the amount of times "Khan" appears in the list
    khan_votes = content.count("Khan")
    #Counts the amount of times "O'Tooley" appears in the list
    otooley_votes = content.count("O'Tooley")
    #Counts the amount of times "Li" appears in the list
    li_votes = content.count("Li")
    #Counts the amount of times "Correy" appears in the list
    correy_votes = content.count("Correy")
    #Calculates total votes
    total_votes = khan_votes + li_votes + correy_votes + otooley_votes
    #Calculates Khan Vote Percentage
    khan_vote_percent = round(((khan_votes / total_votes) * 100), 2)
    #Calculates Correy Vote Percentage
    correy_vote_percent = round(((correy_votes / total_votes) * 100), 2)
    #Calculates Li Vote Percentage
    li_vote_percent = round(((li_votes / total_votes) * 100), 2)
    #Calculates O'Tooley Vote Percentage
    otooley_vote_percent = round(((otooley_votes / total_votes) * 100), 2)
    #If statements to find out who won
    if (khan_votes > otooley_votes and khan_votes > li_votes and khan_votes > correy_votes):
        winner = "Khan"
    elif (otooley_votes> khan_votes and otooley_votes > li_votes and otooley_votes >correy_votes):
        winner = "O'Tooley"
    elif (correy_votes> khan_votes and correy_votes > li_votes and correy_votes> otooley_votes):
        winner = "Correy"
    elif (li_votes> khan_votes and li_votes > correy_votes and li_votes> otooley_votes):
        winner = "O'Tooley"
    #PRINT OUTPUT TO TERMINAL HERE
    #Print "Election Results"
    print("Election Results")
    #Print ----- to seperate title
    print("-------------------------")
    #Print Total Votes
    print("Total Votes: " + str(total_votes))
    #Print ----- to seperate votes from rest of data
    print("-------------------------")
    #Print Khan results to terminal
    print("Khan: " + str(khan_vote_percent) + "%" " (" + str(khan_votes) + ")")
    #Print Correy results to terminal
    print("Correy: " + str(correy_vote_percent) + "%" " (" + str(correy_votes) + ")")
    #Print Li results to terminal
    print("Li: " + str(li_vote_percent) + "%" " (" + str(li_votes) + ")")
    #Print O'Tooley results to terminal
    print("O'Tooley: " + str(otooley_vote_percent) + "%" " (" + str(otooley_votes) + ")")
    #Print Winner
    print("-------------------------")
    print("Winner: " + winner)
    print("-------------------------")


#OUTPUT ANALYSIS TO TXT FILE IN "ANALYSIS" FOLDER
#Define Output File Path
pypoll_output_path = os.path.join("PyPoll", "analysis", "pyPoll_analysis.txt")
outputfile = open(pypoll_output_path, "x")
#Prints Title
outputfile.write("Election Results\n")
outputfile.write("----------------------------\n")
#Prints Total Votes Section
outputfile.write("Total Votes: ")
outputfile.write(str(total_votes))
outputfile.write("\n")
outputfile.write("----------------------------\n")
#Prints Khan's Results
outputfile.write("Khan: ")
outputfile.write(str(khan_vote_percent))
outputfile.write("% (")
outputfile.write(str(khan_votes))
outputfile.write(")")
outputfile.write("\n")
#Prints Correy's Results
outputfile.write("Correy: ")
outputfile.write(str(correy_vote_percent))
outputfile.write("% (")
outputfile.write(str(correy_votes))
outputfile.write(")")
outputfile.write("\n")
#Prints Li's Results
outputfile.write("Li: ")
outputfile.write(str(li_vote_percent))
outputfile.write("% (")
outputfile.write(str(li_votes))
outputfile.write(")")
outputfile.write("\n")
#Prints O'Tooleys's Results
outputfile.write("O'Tooley: ")
outputfile.write(str(otooley_vote_percent))
outputfile.write("% (")
outputfile.write(str(otooley_votes))
outputfile.write(")")
outputfile.write("\n")
outputfile.write("----------------------------\n")
#Prints Winner Value
outputfile.write("Winner: ")
outputfile.write(winner)
outputfile.write("\n")
outputfile.write("----------------------------\n")