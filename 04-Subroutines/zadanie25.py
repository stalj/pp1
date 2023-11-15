greater_than = lambda x, y: True if x > y else False

pair1 = (34, 25)
pair2 = (19, 23)

result1 = greater_than(pair1[0], pair1[1])
result2 = greater_than(pair2[0], pair2[1])

print(f"For pair {pair1}, the result is: {result1}")
print(f"For pair {pair2}, the result is: {result2}")