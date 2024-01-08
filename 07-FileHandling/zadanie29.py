import re
with open("grades.txt", "r") as file:
     lines = file.read()
     x = re.findall("[0-9].[0-9]",lines)
     sum= 0
     for i in x:
          i = float(i)
          sum+=i
print(f"Arithmetic mean of student’s grades: {round(sum/len(x), 2)}")
        
    