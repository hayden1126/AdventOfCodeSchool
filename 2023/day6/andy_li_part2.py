import re
import math

with open("6/large_input.txt") as f:
    lines = f.readlines()
    
time = int("".join(re.findall("\d+", lines[0])))
distance = int("".join(re.findall("\d+", lines[1])))

solve_quadratic = lambda a, b, c: ((-1*b + math.sqrt(b**2 - 4*a*c))/(2*a), (-1*b - math.sqrt(b**2 - 4*a*c))/(2*a))

sols: list[float] = solve_quadratic(-1, time, -1*distance)
wins = math.floor(sols[1]) - math.ceil(sols[0]) + 1
if sols[0].is_integer():
    wins -= 2

print(wins)
