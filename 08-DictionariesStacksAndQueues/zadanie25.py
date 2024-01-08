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

rpn = str(input("Enter formula: "))
for i in rpn:
    if i.isdecimal():
        push(i)
    elif i == "+":
        push(int(pop())+int(pop()))
    elif i == "-":
        pop1 = int(pop())
        pop2= int(pop())
        push(pop2-pop1)
    elif i == "*":
        push(int(pop())*int(pop()))
    elif i == "/":
        pop1 = int(pop())
        pop2 = int(pop())
        push(pop2/pop1)
    if i == "=":
        print(*stack)