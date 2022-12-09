import sys

data = sys.stdin.readlines()
data = [[e[0], int(e.split()[1])] for e in data]

x, y = 0, 4


tail_log = [(x,y)]
position_log = [(x,y)]

for line in data:
    templog = []
    if line[0] == 'R':
        for _ in range(line[1]):
            x += 1
            position_log.append((x,y))
            templog.append((x,y))
    if line[0] == 'L':
        for _ in range(line[1]):
            x -= 1
            position_log.append((x,y))
            templog.append((x,y))
    if line[0] == 'U':
        for _ in range(line[1]):
            y += 1
            position_log.append((x,y))
            templog.append((x,y))
    if line[0] == 'D':
        for _ in range(line[1]):
            y -= 1
            position_log.append((x,y))
            templog.append((x,y))
    
    tail_log += templog[:-1]

