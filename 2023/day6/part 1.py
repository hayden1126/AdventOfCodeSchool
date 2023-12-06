import re
import math

with open("6/input.txt") as f:
    lines = f.readlines()
    
times = [int(i) for i in re.findall("\d+", lines[0])]
distances = [int(i) for i in re.findall("\d+", lines[1])]

solve_quadratic = lambda a, b, c: ((-1*b + math.sqrt(b**2 - 4*a*c))/(2*a), (-1*b - math.sqrt(b**2 - 4*a*c))/(2*a))

output = 1
for i in range(len(times)):
    sols: list[float] = solve_quadratic(-1, times[i], -1*distances[i])
    wins = math.floor(sols[1]) - math.ceil(sols[0]) + 1
    if sols[0].is_integer():
        wins -= 2
    output *= wins

print(output)