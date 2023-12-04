with open('tickets.txt', 'r') as f:
    tickets = f.read().split('\n')

total = 0

for ticket in tickets:
    winners = []
    draw = []
    matches = 0
    points_per = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]

    # make array of winning numbers
    for i in range(2, 30, 3):
        try:
            winners.append(int(ticket[ticket.find(':') + i] + ticket[ticket.find(':') + (i + 1)]))
        except ValueError:
            winners.append(int(ticket[ticket.find(':') + (i + 1)]))

    # make array of drawn numbers
    for j in range(2, 75, 3):
        try:
            draw.append(int(ticket[ticket.find('|') + j] + ticket[ticket.find('|') + (j + 1)]))
        except ValueError:
            draw.append(int(ticket[ticket.find('|') + (j + 1)]))

    # find number of matches
    for number in draw:
        if number in winners:
            matches += 1

    # calculate points with points table
    total += points_per[matches]

print(total)
