import sys

data = sys.stdin.readlines()
data = [e.split(' ') for e in data]

x = 1
cycle = 0
dic = {}


for line in data:
    if line[0].strip() == "noop":
        cycle += 1
        dic[cycle] = x

    elif line[0] == "addx":
        for _ in range(1):
            cycle += 1
            dic[cycle] = x
        
        cycle += 1
        dic[cycle] = x
        x += int(line[1])

def strength(dic, n):
    return n * dic[n]

def sol1(dic):
    sum = 0
    for i in range(20, 220 + 1, 40):
        sum += strength(dic, i)

    return sum

def sol2(dic):
    string = ""
    for cycle, x in dic.items():
        pos = (cycle - 1) % 40
        if (pos % 40 == 0):
            string += '\n'
        if (pos >= x-1 and pos <= x+1):
            string += "#"
        else:
            string += '.'
    return string

print(sol1(dic))
print(sol2(dic))