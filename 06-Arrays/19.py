import random

arr1 = [3,7,1,0,4]
arr2 = [[2,3],[7,1],[0,4]]
arr3 = [7 for i in range(5)] # Puts 5 "7"s in a list
arr4 = [i for i in range(1,10)] # Puts numbers from 1 to 9 in a list
arr5 = [i*2 for i in range(1,10)] # Puts numbers from 1 to 9 in a list, and multiplies them by 2
arr6 = [random.randint(1,20) for i in range(10)] # Puts 10 random numbers(1,20) in a list
arr7 = [[] for i in range(5)] # Puts 5 empty lists in another list
arr8 = [[1 for i in range(2)] for j in range(4)] # Puts 4 lists, filled with 1s, in another list
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]

arr10 = [4,0,3]
arr11 = [0 for iteration in range(15)] # Put ZERO for each ITERATION, 15 times
arr12 = [iteration for iteration in range(1,30)] # Put whatever the iteration is at the moment in a list, range (1-29)
arr13 = [random.randint(0,1) for iteration in range(20)] # Put RANDOM NUMBER(0-1) for each ITERATION, 20 times
arr14 = [[False for iteration in range(2)] for j in range(5)]


print(arr14)