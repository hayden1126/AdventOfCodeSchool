with open('tickets.txt', 'r') as f:
    tickets = f.read().split('\n')

total_tickets = 0
multiplier_list = [1] * 202
card = 0

for ticket in tickets:
    card += 1  # the card we are currently analysing
    winners = []
    draw = []
    matches = 0

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

    # add copies of won numbers to the multiplier list
    for k in range(matches):
        multiplier_list[card + k] += 1 * multiplier_list[card - 1]

# add all the copies together
for cards in multiplier_list:
    total_tickets += cards

print(total_tickets)
