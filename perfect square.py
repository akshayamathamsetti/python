import math
n=int(input('Enter n value:'))
root=int(math.sqrt(n))
if root*root==n:
    print("perfect square")
else:
    print("Not perfect square")
