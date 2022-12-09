import sys

data = sys.stdin.readlines()
data = [[e[0], int(e.split()[1])] for e in data]

x, y = 0, 0
i, j = 0, 0

tail_log = []

def neighbour(i,j,x,y):
    for a in range(-1, 2):
       for b in range(-1, 2):
            if((i+a,j+b) == (x,y)):
                return True
    
    return False

def move():
    for a in range(-1, 2):
       for b in range(-1, 2):
        if(neighbour(i+a,j+b, x,y)):
            i = i+a
            j = j+b



for line in data:
    templog = []
    if line[0] == 'R':
        for _ in range(line[1]):
            x += 1
    if line[0] == 'L':
        for _ in range(line[1]):
            x -= 1
    if line[0] == 'U':
        for _ in range(line[1]):
            y += 1
    if line[0] == 'D':
        for _ in range(line[1]):
            y -= 1
    
    if (neighbour(i,j, x,y)):
        continue
    else:
        move()
        
    tail_log.append((i,j))
