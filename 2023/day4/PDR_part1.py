import re

with open('input.txt', 'r') as file:
	lines = file.read().split('\n')

characters = [list(line) for line in lines]

def adjacent(index, start, end):
	points = []
	if index > 0:
		points += [(index - 1, j) for j in range(start, end)]
	if index < 139:
		points += [(index + 1, j) for j in range(start, end)]
	if start > 0:
		points += [(index, start - 1)]
	if end < 139:
		points += [(index, end)]
	if index > 0 and start > 0:
		points += [(index - 1, start - 1)]
	if index > 0 and end < 139:
		points += [(index - 1, end)]
	if index < 139 and start > 0:
		points += [(index + 1, start - 1)]
	if index < 139 and end < 139:
		points += [(index + 1, end)]
	
	return points

total = 0
for index in range(len(lines)):
	for match in re.finditer(r'\d+', lines[index]):
		points = adjacent(index, match.start(), match.end())
		
		adjacentCharacters = []
		for point in points:
			adjacentCharacters.append(characters[point[0]][point[1]])
		
		if any(character != '.' for character in adjacentCharacters):
			total += int(match.group())
		
print(total)	