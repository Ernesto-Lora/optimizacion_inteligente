import math 
def n(a,b,epsilon):
    return math.log(epsilon/(b-a), 0.618) +1

a = 0
b = 5
epsilon = 1e-3
print(n(a,b,epsilon))