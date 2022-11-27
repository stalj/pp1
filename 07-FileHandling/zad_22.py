import csv

with open('zad_22.txt','r') as csv_file:
    csv_reader=csv.reader(csv_file)

    for line in csv_reader:
        if int(line[2])<30:
            print(line[0],line[1],line[4])

