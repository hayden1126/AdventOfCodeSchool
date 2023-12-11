mapping = {'A': 'a', 'K': 'b', 'Q': 'c', 'J': 'z', 'T': 'e', '9': 'f', '8': 'g', '7': 'h', '6': 'i', '5': 'j', '4': 'k', '3': 'l', '2': 'm'}

def translate(hand):	
	output = ''
	for character in hand:
		output += mapping[character]
		
	return output

def rankPrefix(string):
	counts = [string.count(character) for character in string]
	
	if max(counts) == 5:
		return 'a'
	elif max(counts) == 4:
		return 'b'
	elif 3 in counts and 2 in counts:
		return 'c'
	elif 3 in counts:
		return 'd'
	elif counts.count(2) == 4:
		return 'e'
	elif counts.count(2) == 2:
		return 'f'
	elif counts.count(1) == 5:
		return 'g'
	
	return rankString

def rankString(hand):
	string = translate(hand)
	if 'z' not in string:
		return rankPrefix(string) + string
	else:
		counts = {i: string.count(i) for i in string if i != 'z'}
		
		bestLetter = 'z'
		highestCount = 0
		for key, value in counts.items():
			if value > highestCount:
				bestLetter = key
				highestCount = value
		
		newString = string.replace('z', bestLetter)
		return rankPrefix(newString) + string

lines = open('input.txt', 'r').read().split('\n')
data = [(rankString((l := line.split(' '))[0]), int(l[1])) for line in lines]

data.sort(key=lambda x: x[0], reverse=True)

rank = 1
score = 0
for (hand, bid) in data:
	score += bid * rank
	rank += 1

print(score)