import regex

with open('input.txt', 'r') as file:
    text = file.read()

text = text.replace(";", ",")
lines = text.split('\n')

def power(line):
	draws = line.split(": ")[1].split(", ")
	reds = 0
	greens = 0
	blues = 0
	
	for draw in draws:
		[value, colour] = draw.split(' ')
		if colour == 'red' and int(value) > reds:
			reds = int(value)
		elif colour == 'green' and int(value) > greens:
			greens = int(value)
		elif colour == 'blue' and int(value) > blues:
			blues = int(value)
		
	return reds * greens * blues

total = 0	
for line in lines:
	total += power(line)

print(total)
