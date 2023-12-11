import re
from math import ceil, floor, sqrt
from functools import reduce

data = open('input.txt').read()

list_map = lambda f: lambda x: list(map(f, x))
parse_line = lambda x: re.findall('\d+', x)
to_ints = lambda x: list_map(lambda y: int(y))(x)
to_tuple = lambda x, y: lambda i: (x[i], y[i]) 
to_tuples = lambda x, y: list_map(to_tuple(x, y))(range(len(x)))
parse_data = lambda x: to_tuples(*list_map(to_ints)(list_map(parse_line)(x.split('\n'))))
ways_to_win = lambda x: floor((x[0] + sqrt(x[0] * x[0] - 4 * x[1]))/2) - ceil((x[0] - sqrt(x[0] * x[0] - 4 * x[1]))/2) + 1
product = lambda x: reduce(lambda y, z: y * z, x)

print(product(list_map(ways_to_win)(parse_data(data))))
