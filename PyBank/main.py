import os
import csv
totaltraded = int(0)
mostprofitmonth = "None"
mostprofit = 0
mostlossmonth = "None"
mostloss = 0

csvpath = os.path.join('budget_data.csv')
file = open("budget_data.csv")
numline = len(file.readlines())
#print (numline)#This was a test to see if my script properly 
#measured the lines in the .csv file
with open(csvpath, newline='', encoding="utf8") as csvfile:

#    CSV reader specifies delimiter and variable that holds contents
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvreader)
	for row in csvreader:
		if float(row[1])>0 and float(row[1])>mostprofit:
			mostprofitmonth = str(row[0])
			mostprofit = float(row[1])
		elif float(row[1])<0 and float(row[1])<mostloss:
			mostlossmonth = str(row[0])
			mostloss = float(row[1])			
		totaltraded += float(row[1])
 
nummonths = numline - 1 #As the .csv file was all months minus the header, this was the 
#fastest solution
f= open("Output.txt","w+")
with open("Output.txt", "w") as text_file:
	print("Financial Analysis")
	print("----------------------------")
	print("Total Months: " + str(nummonths))
	print("Total: $" + str(totaltraded))
	print("Average Chance: $" + str(totaltraded/nummonths))
	print("Greatest Increase in Profits: " + mostprofitmonth + "($" + str(mostprofit) + ")")
	print("Greatest Decrease in Profits: " + mostlossmonth + "($" + str(mostloss) + ")")
#	print("Financial Analysis")
	f.write("Financial Analysis" + "\n")
	f.write("----------------------------"+ "\n")
	f.write("Total Months: "+ "\n")
	f.write("Total: $" + str(totaltraded)+ "\n")
	f.write("Average Chance: $" + str(totaltraded/nummonths)+ "\n")
	f.write("Greatest Increase in Profits: " + mostprofitmonth + "($" + str(mostprofit) + ")"+ "\n")
	f.write("Greatest Decrease in Profits: " + mostlossmonth + "($" + str(mostloss) + ")"+ "\n")
# print(str(totaltraded))
# print(mostprofitmonth)
# print(mostprofit)
# print(mostlossmonth)
# print(mostloss)
#Above five lines were tests to see if the program had correctly recorded the needed values
