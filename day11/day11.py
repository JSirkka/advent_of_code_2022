import sys

data = sys.stdin.read().split('\n\n')


def monkey_parse(data):
    data = data.split('\n')
    print(data)
    start_items = data[1].split(':')[1].split(',')
    operation = data[2][-4]
    return data

monkey_parse(data[0])