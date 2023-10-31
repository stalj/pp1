import csv
x=[]
with open("students.csv", "r") as f:
    r = csv.reader(f)
    d=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]
    for i in r:
        for j in i:
            if j in d:
                x.append(i)

for i in range(len(x)):
    print(x[i][0], x[i][1], x[i][-1])