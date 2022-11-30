stack = []
	

def push(value):
    stack.append(value)
push(24)
push(3)
push(6)
print(stack)

def empty():
    return len(stack) == 0

def pop():
    if not empty():
        return stack.pop()
    else:
        return None
pop()
print(stack)


def display():
    for i in range(len(stack)-1,-1,-1):
        print(stack[i])
    print()
display()

