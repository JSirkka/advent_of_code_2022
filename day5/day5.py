import sys

data = sys.stdin.read()
data = data.split('\n\n')


def parse_crates(data):
    data = data.split('\n')
    loops = (len(data[0]) + 1)
    cols = len(data[0]) // 4 + 1
    
    crates = []
    for i in range(cols):
        crates.append("")

    for ele in data[:-1]:
        index = 0
        for i in range(1, loops, 4):
            if ele[i] != ' ':
                crates[index] += ele[i]
            index += 1
    return crates

def parse_line(line):
    line = line.strip().split(' ')
    line = [line[1], line[3], line[5]]
    line = [int(n) for n in line]
    return line

def move_crate(command, crates, rev=True):
    amount, start, end = command
    start -= 1
    end -= 1
    if rev:
        crates[end] = crates[start][:amount][::-1] + crates[end]
    else:
        crates[end] = crates[start][:amount] + crates[end]

    crates[start] = crates[start][amount:]


def sol1(data, crates):
    for line in data:
        move_crate(parse_line(line), crates)
    
    ans = ""
    for ele in crates:
        ans += ele[0]

    return ans

def sol2(data, crates):
    for line in data:
        move_crate(parse_line(line), crates, False)
    
    ans = ""
    for ele in crates:
        ans += ele[0]

    return ans

crates = parse_crates(data[0])

lines = data[1].split('\n')

print(sol1(lines, crates.copy()))
print(sol2(lines, crates.copy()))