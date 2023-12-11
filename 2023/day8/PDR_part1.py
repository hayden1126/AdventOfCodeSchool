import re

with open('input.txt', 'r') as file:
	text = file.read()
	
instructions = (t := text.split('\n\n'))[0]

nodesText = t[1]
nodes = {}
for line in nodesText.strip().split('\n'):
	match = re.search('(\w+) = \((\w+), (\w+)\)', line)
	nodes[match.group(1)] = {'L': match.group(2), 'R': match.group(3)}

node = 'AAA'
count = 0
while node != 'ZZZ':
	for instruction in instructions:
		node = nodes[node][instruction]
		count += 1
		print(node)
		
print(count)
