import os
import csv
csvpath = os.path.join('election_data.csv')
file = open("election_data.csv")
numline = len(file.readlines())
totalvotes = numline - 1
# print(numline)
# print(totalvotes)
khancount = 0
correycount = 0
licount = 0
otooleycount = 0
with open(csvpath, newline='', encoding="utf8") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvreader)
	for row in csvreader:
		if str(row[2]) == "Khan":
			khancount = khancount + 1
		elif str(row[2]) == "Correy":
			correycount = correycount + 1			
		elif str(row[2]) == "Li":
			licount = licount + 1
		elif str(row[2]) == "O'Tooley":
			otooleycount = otooleycount + 1
f= open("Output.txt", "w+")
with open("Output.txt", "w") as text_file:
	print("Election Results")
	print("-------------------------")
	print("Total Votes: " + str(totalvotes))
	print("-------------------------")
	print("Khan: " + str("%.0f%%" % (100 * khancount/totalvotes)) + " (" + str(khancount) + ")")
	print("Correy: " + str("%.0f%%" % (100 * correycount/totalvotes)) + " (" + str(correycount) + ")")
	print("Li: " + ("%.0f%%" % (100 * licount/totalvotes)) + " (" + str(licount) + ")")
	print("O'Tooley: " + ("%.0f%%" % (100 * otooleycount/totalvotes)) + " (" + str(otooleycount) + ")")
# Start printing to file here
	f.write("Election Results"+ "\n")
	f.write("-------------------------"+ "\n")
	f.write("Total Votes: " + str(totalvotes)+ "\n")
	f.write("-------------------------"+ "\n")
	f.write("Khan: " + str("%.0f%%" % (100 * khancount/totalvotes)) + " (" + str(khancount) + ")"+ "\n")
	f.write("Correy: " + str("%.0f%%" % (100 * correycount/totalvotes)) + " (" + str(correycount) + ")"+ "\n")
	f.write("Li: " + ("%.0f%%" % (100 * licount/totalvotes)) + " (" + str(licount) + ")"+ "\n")
	f.write("O'Tooley: " + ("%.0f%%" % (100 * otooleycount/totalvotes)) + " (" + str(otooleycount) + ")"+ "\n")

