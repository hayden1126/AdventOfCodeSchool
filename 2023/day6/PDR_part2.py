import re
from math import ceil, floor, sqrt
from functools import reduce

data = open('input.txt').read()

list_map = lambda f: lambda x: list(map(f, x))
parse_line = lambda x: int(''.join(re.findall('\d+', x)))
ways_to_win = lambda x: floor((x[0] + sqrt(x[0] * x[0] - 4 * x[1]))/2) - ceil((x[0] - sqrt(x[0] * x[0] - 4 * x[1]))/2) + 1

r = ways_to_win(list_map(parse_line)(data.split('\n')))
print(r)