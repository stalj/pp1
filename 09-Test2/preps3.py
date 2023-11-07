def f(dictionary, x, y):
  # Initialize a variable to store the sum
  sum = 0
  
  # Iterate through the items in the dictionary
  for key, value in dictionary.items():
    # Check if the key is in the range x to y
    if x <= value <= y:
      # If so, add the value to the sum
      sum += value
      
  # Return the sum
  return sum

f({"arr1":[4,5,6], "arr2":[7,5]}, 5, 6) 

