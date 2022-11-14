import numpy as np
def month(n):
    month=np.array(["january","february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"])
    return(month[n-1])
print(month(5))