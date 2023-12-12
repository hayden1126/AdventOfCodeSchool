from functools import reduce

with open('input.txt', 'r') as file:
	lines = file.read().strip().split('\n')

sequences = [[int(x) for x in line.split(' ')] for line in lines]

differences = lambda x: [x[i + 1] - x[i] for i in range(len(x) - 1)]

def isRepeating(sequence):
	return sequence.count(sequence[0]) == len(sequence)

def previous_term(sequence):
	first_terms = [sequence[0]]
	while not isRepeating(sequence):
		sequence = differences(sequence)
		first_terms.append(sequence[0])
	
	return reduce(lambda x, y: y - x, reversed(first_terms))


r = sum([previous_term(sequence) for sequence in sequences])
print(r)