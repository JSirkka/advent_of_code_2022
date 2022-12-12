import sys
import math

data = sys.stdin.read().split('\n\n')


def monkey_parse(data):
    data = data.split('\n')
    start_items = data[1].split(':')[1].split(',')
    start_items = [int(n) for n in start_items]
    operation = data[2].split('=')[-1].strip()
    test_factor = int(data[3].split(' ')[-1])
    true = int(data[4].split(' ')[-1])
    false = int(data[5].split(' ')[-1])

    return [start_items, operation, test_factor, true, false, 0]

def monkey_throw(monkey, div=True):
    start_items, operation, test_factor, true, false, inspected = monkey
    divs = [e[2] for e in monkeys]
    lcm = math.lcm(divs[0], divs[1])
    for n in divs[2:]:
        lcm = math.lcm(lcm, n)

    while start_items:
        old = start_items.pop(0)
        item = eval(operation)
        if(div):
            item = item // 3
        
        item %= lcm
        
        if(item % test_factor == 0):
            monkeys[true][0].append(item)
        else:
            monkeys[false][0].append(item)
        monkey[-1] += 1
            
        
def sol1(monkeys):
    n = 20
    for _ in range(n):
        for monkey in monkeys:
            monkey_throw(monkey)

    inspect = []
    for monkey in monkeys:
        inspect.append(monkey[-1])

    a, b = sorted(inspect, reverse=True)[:2]
    return a * b


monkeys = [monkey_parse(e) for e in data]
#print(sol1(monkeys))

def sol2(monkeys):
    n = 10000
    for _ in range(n):
        for monkey in monkeys:
            monkey_throw(monkey, div=False)
    
    inspect = []
    for monkey in monkeys:
        inspect.append(monkey[-1])

    a, b = sorted(inspect, reverse=True)[:2]
    return a * b

print(sol2(monkeys))