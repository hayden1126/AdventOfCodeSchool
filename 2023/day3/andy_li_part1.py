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
specialCoords: list[tuple[int, int]] = []
y = 0
for line in lines:
    found = re.finditer("\d+", line)
    for number in found:
        numbers.append(Number(int(number.group()), [(x, y) for x in range(*number.span())]))
    found = re.finditer("[^0123456789.]", line)
    for char in found:
        specialCoords.append((char.start(), y))
    y += 1

#print([number.value for number in numbers])
#print(specialCoords)

output = 0
for number in numbers:
    for coord in specialCoords:
        if number.isAdjacent(coord):
            output += number.value
            #print(number.value)
            break

print(output)
