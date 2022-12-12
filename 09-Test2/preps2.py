import csv
import re

with open("test.csv", "r") as f:
    a=csv.reader(f, delimiter=',')

    for i in a:
        for j in i:
            csv.DictReader