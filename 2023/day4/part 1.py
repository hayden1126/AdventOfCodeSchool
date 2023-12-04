import re

with open("4/input.txt") as f:
    lines = [i.strip() for i in f.readlines()]

output = 0
for line in lines:
    line = line.split(": ")
    line[0] = line[0].replace("Card ", "")
    id = int(line[0])
    line = line[1].split("|")
    win = [int(i) for i in re.findall("\d+", line[0])]
    guess = [int(i) for i in re.findall("\d+", line[1])]
    match = len(set(win) & set(guess))
    output += 0 if match == 0 else 2**(match-1)
print(output)