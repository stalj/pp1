def f (binary_number):
    for digit in binary_number:
        if digit not in '01':
            return False
    return True
