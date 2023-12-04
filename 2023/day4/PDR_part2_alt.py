import re, functools

print((f := lambda u, v: u if len(v) == 0 else f(u + v[0][1], [(v[i][0], v[i][1] + v[0][1]) if i <= v[0][0] else v[i] for i in range(1, len(v))]))(0, [(sum([1 for w in z if w]) if any(z) else 0, 1) for z in [[y[1][j] in y[0] for j in range(len(y[1]))] for y in [[[int(x) for x in re.findall(r'\d+', string)] for string in line.split(':')[1].split('|')] for line in open('input.txt', 'r').read().split('\n')]]]
))
