with open("input.txt") as f:
    data = [i.strip() for i in f.readlines()]
    
output = []

cubetotal = {
    "red": 12,
    "green": 13,
    "blue": 14
}

for datum in data:
    datum = datum.split(": ")
    id = int(datum[0][5:])
    datum = datum[1]
    datum = datum.split("; ")
    flag = False
    for datumum in datum:
        cube = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        datumum = datumum.split(", ")
        for iranoutofnames in datumum:
            iranoutofnames = iranoutofnames.split(" ")
            cube[iranoutofnames[1]] = int(iranoutofnames[0])
        for key in cubetotal.keys():
            if cube[key] > cubetotal[key]:
                flag = True
                break
        if flag:
            break
    if not flag:
        output.append(id)

print(sum(output))