

def rankString(hand):
	map = {'A': 'a', 'K': 'b', 'Q': 'c', 'J': 'd', 'T': 'e', '9': 'f', '8': 'g', '7': 'h', '6': 'i', '5': 'j', '4': 'k', '3': 'l', '2': 'm'}
	
	rankString = ''
	for character in hand:
		rankString += map[character]
		
	counts = [rankString.count(character) for character in rankString]
	
	if max(counts) == 5:
		rankString = 'a' + rankString
	elif max(counts) == 4:
		rankString = 'b' + rankString
	elif 3 in counts and 2 in counts:
		rankString = 'c' + rankString
	elif 3 in counts:
		rankString = 'd' + rankString
	elif counts.count(2) == 4:
		rankString = 'e' + rankString
	elif counts.count(2) == 2:
		rankString = 'f' + rankString
	elif counts.count(1) == 5:
		rankString = 'g' + rankString
	
	return rankString
		
lines = open('input.txt', 'r').read().split('\n')
data = [(rankString((l := line.split(' '))[0]), int(l[1])) for line in lines]
data.sort(key=lambda x: x[0], reverse=True)

rank = 1
score = 0
for (hand, bid) in data:
	print(f'bid {bid} * rank {rank} =', bid * rank)
	score += bid * rank
	rank += 1

print('score:', score)
	