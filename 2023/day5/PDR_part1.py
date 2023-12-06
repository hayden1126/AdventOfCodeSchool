import re
from functools import reduce

data = open('input.txt', 'r').read()

A = lambda f: lambda x: list(map(f, x))
B = lambda f, g: lambda x: g(f(x))
C = lambda l: reduce(B, l, lambda x: x)
D = lambda u: A(lambda x: int(x))(u.split('\n\n')[0].split(": ")[1].split(' ')) 
E = lambda u: A(lambda x: A(lambda y: A(lambda z: int(z))(y.split(' ')))(x.split('\n')[1:]))(u.split('\n\n')[1:])
F = lambda x, y: x | {(y[1], y[1] + y[2] - 1): (y[0], y[0] + y[2] - 1)}
G = lambda x: reduce(F, x, {})
H = lambda y: lambda x: x if len(a := list(filter(lambda z: z[0] <= x <= z[1], y.keys()))) == 0 else y[a[0]][0] + x - a[0][0]
I = lambda y: A(lambda x: H(x))(A(G)(E(y)))
J = lambda x: min(A(C(I(x)))(D(x)))

print(J(data))