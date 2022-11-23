def findLargest(arr):
    secondLargest = 0
    largest = min(arr) 
 
    for i in range(len(arr)):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        else:
            secondLargest = max(secondLargest, arr[i])
    return secondLargest
 
 
# Calling above method over this array set
print(findLargest([5,1,9,6,1]))