import csv 

csv.register_dialect('myDialect', delimiter='/', quoting=csv.QUOTE_NONE) 
  

with open('students.txt.csv', newline='') as myFile: 
 reader = csv.reader(myFile, dialect='myDialect') 
 for row in reader: 
  print(row) 