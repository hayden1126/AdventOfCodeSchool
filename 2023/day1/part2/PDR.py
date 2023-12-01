import regex

with open('input.txt', 'r') as file:
	lines = file.read().split('\n')
	
def stringToInt(string):
	numberWords = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	
	try:
		value = int(string)
	except:
		value = numberWords.index(string)
		
	return value

total = 0

for line in lines:
	pattern = r'\d|one|two|three|four|five|six|seven|eight|nine'
	digits = regex.findall(pattern, line, overlapped=True)
	firstDigit = digits[0]
	lastDigit = digits[-1]
	value = stringToInt(firstDigit) * 10 + stringToInt(lastDigit)
	total += value
	
print(total)