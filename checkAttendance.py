__author__ = "Dan Shen"
__version__ = "1.1"

import csv, sys

# File will be named by month.day.csv since that is how the buzzcard scanner names it
date = raw_input('Enter the class date that you would want to check. (Ex: 1/18) \n')
month,day = date.strip().split("/")

# Checking whether the file exists or not, and then converts to a set for faster lookup
try:
	with open(month + '.' + day + '.csv') as f:
		students = f.read().splitlines()
	f.close()
	attendance = set(students)
except IOError:
	print("CSV file not found. Reconfirm the entered date and presence of the CSV files.")
	sys.exit(0)
	
# Opening full roster, which is in alphabetical order, and prints out the names of those who attended class
print 'Students who attended class on ' + date + '\n'
f2 = open('Roster.csv')
roster = csv.reader(f2)
studentNames = open('students' + month + '.' + day + '.txt','w')

for GTid,lastName,firstName in roster:
	if GTid in attendance:
		print(lastName + ', ' + firstName)
		studentNames.write("%s, %s\n" %(lastName,firstName))

f2.close()
studentNames.close()