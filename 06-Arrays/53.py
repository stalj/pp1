def identity_matrix(number):
    arr = [[0 for i in range(number)] for j in range(number)]

    # change 0 to 1 diagonally
    n = 0
    for list in arr:
        list[n] = 1
        n += 1


    # print the damned thing
    for list in arr:
        for num in list:
            print(num, end=" ")
        print()

identity_matrix(8)