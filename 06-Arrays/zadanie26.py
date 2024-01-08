arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
print('Names:', *arr, sep = ' ')
longest_name = arr[0]
a = 0
for i in arr:
    if len(arr[a])>len(longest_name):
        longest_name = arr[a]
    a+=1
print(f"Longest name: {longest_name}")