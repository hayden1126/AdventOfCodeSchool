with open("5/input.txt") as f:
    lines = f.read().split("\n\n")

seeds = lines[0]
seeds = seeds.split(": ")[1].split(" ")

seedData = [{"seed": int(seed)} for seed in seeds]


maps = lines[1:]
for map in maps:
    map = map.split(" map:\n")
    convert = map[0].split("-to-")
    keys = []
    for row in map[1].split("\n"):
        row = [int(i) for i in row.split(" ")]
        keys.append({
            "start": row[1],
            "end": row[1]+row[2]-1,
            "delta": row[0] - row[1]
        })
    for seed in seedData:
        value = int(seed[convert[0]])
        output = value
        for key in keys:
            if key["start"] <= value and value <= key["end"]:
                output += key["delta"]
                break
        seed[convert[1]] = output

print(min([seed["location"] for seed in seedData]))
