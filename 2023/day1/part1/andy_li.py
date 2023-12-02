with open("1/input.txt") as f:
    data = [i.strip() for i in f.readlines()]
output = []

for datum in data:
    x = 0
    y = 0
    for i in range(len(datum)):
        if datum[i].isdigit():
            x = datum[i]
            break
    for i in range(-1, -len(datum)-1, -1):
        if datum[i].isdigit():
            y = datum[i]
            break
    output.append(int(x + y))
print(sum(output))