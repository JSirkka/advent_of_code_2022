import sys

data = sys.stdin.read().split('\n\n')
data = [[int(p) for p in e.split()] for e in data]
data = [sum(e) for e in data]
data = sorted(data, reverse=True)

def sol1():
    print(data[0])

def sol2():
    print(sum(data[:3]))

