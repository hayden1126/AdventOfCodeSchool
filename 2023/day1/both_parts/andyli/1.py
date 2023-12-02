with open("1/input.txt") as f:
    data = [i.strip() for i in f.readlines()]
output = []

#part 1
"""
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
"""

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for datum in data:
    x = 0
    y = 0
    for i in range(len(datum)):
        flag = False
        if datum[i].isdigit():
            x = datum[i]
            break
        for number in numbers:
            if datum[i: i+len(number)] == number:
                x = str(numbers.index(number) + 1)
                flag = True
                break
        if flag:
            break
    for i in range(len(datum)-1, -1, -1):
        flag = False
        if datum[i].isdigit():
            y = datum[i]
            break
        for number in numbers:
            if datum[i: i+len(number)] == number:
                y = str(numbers.index(number) + 1)
                flag = True
                break
        if flag:
            break
    output.append(int(x + y))
print(sum(output))