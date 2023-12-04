import regex

with open('input.txt', 'r') as file:
	lines = file.read().split('\n')

total = 0

for line in lines:
	digits = regex.findall('\d', line)
	firstDigit = digits[0]
	lastDigit = digits[-1]
	value = int(firstDigit + lastDigit)
	total += value
	
print(total)