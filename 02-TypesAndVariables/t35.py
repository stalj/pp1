def tree_cut():
    circumference = float(input("Enter tree circumference: "))
    diameter = circumference/3.14
    if diameter >= 50:
        check = True
    else:
        check = False
    result = f"Tree can be cut down: {check}"

    return result

print(tree_cut())