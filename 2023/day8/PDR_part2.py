import re
from math import lcm

with open('input.txt', 'r') as file:
	text = file.read()
	
instructions = (t := text.split('\n\n'))[0]

nodesText = t[1]
maps = {}
startingNodes = []
for line in nodesText.strip().split('\n'):
	match = re.search('(\w+) = \((\w+), (\w+)\)', line)
	maps[match.group(1)] = {'L': match.group(2), 'R': match.group(3)}
	if match.group(1)[2] == 'A':
		startingNodes.append(match.group(1))

counts = []
for startingNode in startingNodes:
	node = startingNode
	count = 0
	while node[2] != 'Z':
		for instruction in instructions:
			node = maps[node][instruction]
			count += 1
			print(node)
	counts.append(count)

print(lcm(*counts))