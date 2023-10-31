def f6(g, n1,n2):
    import csv
    a=[]
    with open('test.csv') as csv_file:
        a = csv.reader(csv_file, delimiter = ',')
        for i in a:
            if i[-2]=="Ford":
                print(i)
print(f6("male", "Ford", "a"))