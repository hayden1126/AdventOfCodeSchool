import re, functools

print(((lambda f: (lambda x: f(lambda *args: x(x)(*args)))(lambda x: f(lambda *args: x(x)(*args))))(lambda f: lambda x: x[0] if len(x[1]) == 0 else f((x[0] + x[1][0][1], [(x[1][i][0], x[1][i][1] + x[1][0][1]) if i <= x[1][0][0] else x[1][i] for i in range(1, len(x[1]))]))))((0, [(sum([1 for w in z if w]) if any(z) else 0, 1) for z in [[y[1][j] in y[0] for j in range(len(y[1]))] for y in [[[int(x) for x in re.findall(r'\d+', string)] for string in line.split(':')[1].split('|')] for line in open('input.txt', 'r').read().split('\n')]]])))
