import re, functools

print(sum([functools.reduce(lambda x, y: x * y, [2 for w in z if w]) // 2 if any(z) else 0 for z in [[y[1][j] in y[0] for j in range(len(y[1]))] for y in [[[int(x) for x in re.findall(r'\d+', string)] for string in line.split(':')[1].split('|')] for line in open('input.txt', 'r').read().split('\n')]]]))
