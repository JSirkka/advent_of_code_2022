import sys

data = sys.stdin.readlines()
data = [e.split() for e in data]



def strat1(game):
    trans = {'A':0, 'B':1, 'C':2}
    scores = {'X':0, 'Y':1,'Z':2}

    elf, player = game
    elf = trans.get(elf)
    player = scores.get(player)

    score = player + 1

    if (elf == player):
        score += 3
    
    if ((elf + 1) % 3 == player):
        score += 6
    
    return score

def strat2(game):
    trans = {'A':0, 'B':1, 'C':2}
    elf, player = game
    elf = trans.get(elf)
    choice = 0
    score = 0
     
    if(player=='X'):
        choice = (elf - 1) % 3
    
    if(player=='Y'):
        choice = elf
        score += 3

    if(player=='Z'):
        choice = (elf + 1) % 3
        score += 6

    score += (choice + 1)
    
    return score


def sol1(data):
    sum = 0
    for game in data:
        sum += strat1(game)

    return sum

def sol2(data):
    sum = 0
    for game in data:
        sum += strat2(game)

    return sum

#print(sol1(data))
print(sol2(data))