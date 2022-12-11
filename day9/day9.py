import sys

def neighbour(a, b):
    x,y = a
    i,j = b
    for a in range(-1, 2):
       for b in range(-1, 2):
            if (i+a,j+b) == (x,y):
                return True
    
    return False

def move(a, b):
    x,y = a
    i,j = b
    for c in range(-1, 2):
       for d in range(-1, 2):
        if(neighbour([i+c, j+d], b)):
            return( [i+c, j+d] )
    
def move_head():
    global pos, tail_pos
    if(not neighbour(tail_pos, pos)):
        tail_pos = move(tail_pos, pos)

    tail_log.append(tail_pos)

data = sys.stdin.readlines()
data = [[e[0], int(e.split()[1])] for e in data]

pos = [0,0]
tail_pos = [0,0]

tail_log = []

for line in data:
    if line[0] == 'R':
        for _ in range(line[1]):
            pos[0] += 1
            move_head()
    
    if line[0] == 'L':
        for _ in range(line[1]):
            pos[0] -= 1
            move_head()

    if line[0] == 'U':
        for _ in range(line[1]):
            pos[1] += 1     
            move_head()

    if line[0] == 'D':
        for _ in range(line[1]):
            pos[1] -= 1
            move_head()
    
print(len(set([tuple(i) for i in tail_log])))