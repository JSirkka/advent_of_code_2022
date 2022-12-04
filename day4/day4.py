import sys

data = sys.stdin.readlines()
data = [e.strip().split(',') for e in data]
data = [[p.split('-') for p in e] for e in data]

def overlap(ranges):
    ranges = [[int(e) for e in p] for p in ranges]
    a, b = ranges[0]
    c, d = ranges[1]

    return((a <= c and b >= d) or (c <= a and d >= b))

    if a <= c:
        if b >= d:
            return True

    if c <= a:
        if d >= b:
            return True

    return False

def intersect(ranges):
    ranges = [[int(e) for e in p] for p in ranges]
    a, b = ranges[0]
    c, d = ranges[1]
    set1 = set(range(a,b+1))
    set2 = set(range(c,d+1))

    intersect = set.intersection(set1, set2)
    return (len(intersect) > 0)


def sol1(data):
    count = 0
    for ele in data:
        if overlap(ele):
            count += 1
    
    return count

def sol2(data):
    count = 0
    for ele in data:
        if intersect(ele):
            count += 1
    
    return count



print(sol1(data))
print(sol2(data))