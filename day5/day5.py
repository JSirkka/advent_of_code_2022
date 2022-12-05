
import sys

test_crates =[
    'NZ',
    'DCM',
    'P'
]

crates = [
    'TRDHQNPB',
    'VTJBGW',
    'QMVSDHRN',
    'CMNZP',
    'BZD',
    'ZWCV',
    'SLQVCNZG',
    'VNDMJGL',
    'GCZFMPT'
]

data = sys.stdin.readlines()

def parse_line(line):
    line = line.strip().split(' ')
    line = [line[1], line[3], line[5]]
    line = [int(n) for n in line]
    return line

def move_crate(command, rev=True):
    amount, start, end = command
    if rev:
        crates[end - 1] = crates[start - 1][:amount][::-1] + crates[end - 1]
    else:
        crates[end - 1] = crates[start - 1][:amount] + crates[end - 1]

    crates[start - 1] = crates[start - 1][amount:]


def sol1(data):
    for line in data:
        move_crate(parse_line(line))
    
    ans = ""
    for ele in crates:
        ans += ele[0]

    return ans

def sol2(data):
    for line in data:
        move_crate(parse_line(line), False)
    
    ans = ""
    for ele in crates:
        ans += ele[0]

    return ans

#print(sol1(data)) #Do some work with immutability here
print(sol2(data))