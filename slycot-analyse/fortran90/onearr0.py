import numpy as np
import onearr0

a = np.array([1.0, 2.0])
b = np.array([3.0, 4.0])

n = 2
m = 2

print("main", a,b)
onearr0.foo(n,m,a,b)
print("main", a,b)