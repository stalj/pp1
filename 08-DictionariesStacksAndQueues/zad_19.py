import zad_18

# a.	Display stack
# b.	Put the number 2 on the stack
# c.	Put the number 14 on the stack
# d.	Put the number 9 on the stack
# e.	Display stack
# f.	Get element from stack
# g.	Display stack
# h.	Put the number 31 on the stack
# i.	Put the number 6 on the stack
# j.	Display stack
# k.	Get two elements from stack
# l.	Display stack

print(zad_18.stack)
zad_18.stack.append(2)
zad_18.stack.append(14)
zad_18.stack.append(9)
print(zad_18.stack)
zad_18.stack.pop(1)
print(zad_18.stack)
zad_18.stack.append(31)
zad_18.stack.append(6)
print(zad_18.stack)
zad_18.stack.pop(3)
zad_18.stack.pop(0)
print(zad_18.stack)