iteration = 1
string = "0 1"

num_prev = 0
num_next = 1

while iteration <= 19:
    num_current = num_prev + num_next
    string += f" {num_current}"

    num_prev = num_next
    num_next = num_current

    iteration += 1

print(string)
