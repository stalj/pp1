import calendar
def month(n):
    for n in range(1,13):
       print(n, ":", calendar.month_abbr[n], "-", calendar.month_name[n])

n=7
print(n, ":", calendar.month_abbr[n], "-", calendar.month_name[n])