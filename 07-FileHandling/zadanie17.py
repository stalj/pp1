with open("30linesoftext.txt", 'r') as file:
    lines = file.readlines()

total_lines = len(lines)
current_line = 0

while current_line < total_lines:
    for i in range(5):
        if current_line < total_lines:
            print(lines[current_line].strip())
            current_line += 1
    
    input("Press Enter to continue...")