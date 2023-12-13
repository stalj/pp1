# with open("some_file.txt") as f:
#     for _ in range(5):
#         line = f.readline()
#         if not line:
#             break
#         print(line.strip())

# with open("some_file.txt") as f:
#     lines = f.readlines()
#     for line in lines[:5]:
#         print(line.strip())

var = True
start = 0
end = 5

while var == True:


    with open("some_file.txt") as f:
        lines = f.readlines()  # This creates a list ["whatever\n", "whatever\n"]
        for line in lines[start:end]:  # This prints out lines 6-10
            if not line:
                break
            else:
                print(line.strip())
        input_var = input()

        if input_var == "":
            start += 5
            end += 5

        if start > 25 and end > 30:
            var = False
