import re

with open("3/input.txt") as f:
    lines = [i.strip() for i in f.readlines()]

class Number:
    def __init__(self, value: int, coordinates: list[tuple[int, int]]):
        self.value = value
        self.coordinates = coordinates
    def isAdjacent(self, coordinate: tuple[int, int]):
        adjacent = {
            (coordinate[0]-1, coordinate[1]-1),
            (coordinate[0]-1, coordinate[1]),
            (coordinate[0]-1, coordinate[1]+1),
            (coordinate[0], coordinate[1]-1),
            (coordinate[0], coordinate[1]),
            (coordinate[0], coordinate[1]+1),
            (coordinate[0]+1, coordinate[1]-1),
            (coordinate[0]+1, coordinate[1]),
            (coordinate[0]+1, coordinate[1]+1)
        }
        return bool(set(self.coordinates) & adjacent)
    
    def __str__(self):
        return "Number(value={value}, coordinates={coordinates})".format(value = str(self.value), coordinates = str(self.coordinates))

numbers: list[Number] = []
gearCoords: list[tuple[int, int]] = []
y = 0
for line in lines:
    found = re.finditer("\d+", line)
    for number in found:
        numbers.append(Number(int(number.group()), [(x, y) for x in range(*number.span())]))
    found = re.finditer("[*]", line)
    for char in found:
        gearCoords.append((char.start(), y))
    y += 1

output = 0
for gear in gearCoords:
    product = 1
    numbernumbers = 0
    for number in numbers:
        if number.isAdjacent(gear):
            product *= number.value
            numbernumbers += 1
    if numbernumbers == 2:
        output += product

print(output)
