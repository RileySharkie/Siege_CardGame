import random
import csv
from fuzzywuzzy import process


#load card file
filename = "wildDeck.csv"

fields = []
rows = []

with open(filename,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

print("# of rows: %d"%(csvreader.line_num))

#defines column 0
col = [row[0].lower() for row in rows]

#convert all col 0 values to lower case
col0_lower = [x.lower() for x in col]

while True:
    search_name = input("\nEnter A Card (or 'quit' to exit): \n").lower()
    if search_name == 'quit':
        break
    #find closest matches to the input using fuzzywuzzy
    matches = process.extract(search_name.lower(), col0_lower, limit=5)

# print the closest matches if the input value is not found
    if search_name.lower() not in col0_lower:
        print("Value %s not found \n" % search_name)
        print("Closest matches:\n")
        for match in matches:
            match_index = col0_lower.index(match[0])
            print("%s (score: %d)" % (rows[match_index][0], match[1]))
    else:
    # search for the input value in the lowercase row 0
        found = False
        for i,val in enumerate(col0_lower):
            if val == search_name.lower():
                print("Found %s " % search_name)
                found = True
                break
        if not found:
            print("Value %s not found in row 0." % search_value)