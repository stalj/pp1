stack = []

def push(value):
    stack.append(value)

def pop():
    if not empty():
        return stack.pop()
    else:
        return None
    
def empty():
    return len(stack) == 0

def convert_to_binary(number):
    a = number
    while a > 0:
        remainder = a % 2
        push(remainder)
        a //= 2

    binary_number = ""
    while not empty():
        binary_digit = str(pop())
        binary_number += binary_digit

    print("Natural number:", number)
    print("Binary number:", binary_number)

convert_to_binary(18)
