def calculate(text: str, letter: str):
    count = 0
    for iteration in text:
        if iteration == letter:
            count += 1
        else:
            continue
    return count