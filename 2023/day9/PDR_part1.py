with open('input.txt', 'r') as file:
	lines = file.read().strip().split('\n')

sequences = [[int(x) for x in line.split(' ')] for line in lines]

differences = lambda x: [x[i + 1] - x[i] for i in range(len(x) - 1)]

def isRepeating(sequence):
	return sequence.count(sequence[0]) == len(sequence)

def next_term(sequence):
	last_terms = [sequence[-1]]
	while not isRepeating(sequence):
		sequence = differences(sequence)
		last_terms.append(sequence[-1])
	
	return sum(last_terms)

r = sum([next_term(sequence) for sequence in sequences])
print(r)