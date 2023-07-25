import numpy as np
import scalar0

a = 1.0
b = 2.0
c = 3.0

print("main", a,b,c)
scalar0.foo(a,b,c)
print("main", a,b,c)
print("------------")

a = np.array(1.0)
b = np.array(2.0)
c = np.array(3.0)

print("main", a,b,c)
scalar0.foo(a,b,c)
print("main", a,b,c)
print("------------")

a = np.array([1.0])
b = np.array([2.0])
c = np.array([3.0])

print("main", a,b,c)
scalar0.foo(a,b,c)
print("main", a,b,c)
print("------------")