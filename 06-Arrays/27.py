def star(n):
    return "*" * n


arr = [12, 6, 4, 9, 10]
index = 0

while index < len(arr):
    print(f"{arr[index]}: {star(arr[index])}")
    index += 1