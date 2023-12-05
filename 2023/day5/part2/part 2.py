with open("5/input.txt") as f:
    lines = f.read().split("\n\n")

seeds = lines[0]
seeds = seeds.split(": ")[1].split(" ")
seeds = [int(i) for i in seeds]
seeds = [(seeds[i], seeds[i]+seeds[i+1]-1) for i in range(0, len(seeds), 2)]

seedData = [(int(seed[0]), int(seed[1])) for seed in seeds]

maps = lines[1:]
for map in maps:
    map = map.split(" map:\n")
    keys = []
    for row in map[1].split("\n"):
        row = [int(i) for i in row.split(" ")]
        keys.append({
            "start": row[1],
            "end": row[1]+row[2]-1,
            "delta": row[0] - row[1]
        })
    seedDataNew = []
    while len(seedData) > 0:
        seed = seedData[0]
        seedData = seedData[1:]
        value = seed
        flag = True
        for key in keys:
            if key["start"] <= value[0] and value[1] <= key["end"]:
                seedDataNew.append((value[0] + key["delta"], value[1] + key["delta"]))
                flag = False
                break
            elif key["start"] <= value[0] and value[0] <= key["end"]:
                seedDataNew.append((value[0] + key["delta"], key["end"] + key["delta"]))
                seedData.append((key["end"]+1, value[1]))
                flag = False
                break
            elif key["start"] <= value[1] and value[1] <= key["end"]:
                seedDataNew.append((key["start"] + key["delta"], value[1] + key["delta"]))
                seedData.append((value[0], key["start"]-1))
                flag = False
                break
            elif key["start"] < value[0] and key["end"] > value[1]:
                seedDataNew.append((key["start"] + key["delta"], key["end"] + key["delta"]))
                seedData.append((value[0], key["start"]-1))
                seedData.append((key["end"]+1, value[1]))
                flag = False
                break
        if flag:
            seedDataNew.append(seed)
    seedData = seedDataNew

# print(seedData)
print(min([seed[0] for seed in seedData]))