totalIDs = 0
currentID = 0
colors = ['red','green','blue']
colornums = {
  'red':12,
  'green':13,
  'blue':14,
}
powersets=[]
max_colors=[0,0,0]

def filterNumbers(string):
  g = list(string)
  r = ''
  for i in range(len(g)):
    try:
      int(g[i])
    except ValueError:
      g[i]=""
  for i in g:
    r=r+i
  return r

with open('input','r') as f:
  lines = f.read().split("\n")

for line in range(100):
  lines[line] = lines[line].split(": ")
  lines[line][0] = int(filterNumbers(lines[line][0]))
  lines[line][1] = lines[line][1].split("; ")
  for i in range(len(lines[line][1])):
    lines[line][1][i]=lines[line][1][i].split(', ')

for line in lines:
  currentpowerset = 1
  currentID = int(line[0])
  max_colors=[0,0,0]
  for roll in line[1]:
    for value in roll:
      for i in colors:
        if i in value:
          #part 1
          # if int(filterNumbers(value)) > colornums[i]:
          #   totalIDs+=currentID
          #   currentID=0
          #part2
          if int(filterNumbers(value)) > max_colors[colors.index(i)]:
            max_colors[colors.index(i)] = int(filterNumbers(value))
  for k in max_colors:
    currentpowerset*=k
  powersets.append(currentpowerset)
sum = 0
for i in powersets:
  sum+=i
print(sum)
  