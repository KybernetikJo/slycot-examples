import numpy as np
import onearr0

a = np.array([1.0, 1.0])
b = np.array([2.0, 2.0])
c = np.array([3.0, 3.0])

n = 2
m = 2
o = 2

a = np.array([1.0])
b = np.array([2.0])
c = np.array([3.0])

n = 1
m = 1
o = 1

print("main", a,b,c)
onearr0.foo(n,m,o,a,b,c)
print("main", a,b,c)