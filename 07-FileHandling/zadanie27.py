import re 

with open('grades.txt') as file:
    grades = re.findall('\d+\.\d+', file.read())
    print(f'ilość: {len(grades)}')
    sum=0
    for i in grades:
        i=float(i)
        sum+=i
    print(f'summa: {sum}')
    print(f'arithmetic mean of student’s grades: {sum/len(grades)}')
