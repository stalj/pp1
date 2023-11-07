def month(n):
    list = ["January", "February", "March", "April", "Mai", "June" , "July", "August", "September", "October", "November", "December"]
    for i in range(12):
        list[i] = list[n-1]

    print(list[n-1])

month(1)
month(2)
month(11)
month(12)