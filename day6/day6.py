import sys

data = sys.stdin.read().strip()

def sol1(data, n):
    for i in range(len(data) - n - 1):
        my_set = set(data[i:i+n])
        if len(my_set) == n:
            return i + n

print(sol1(data, 4))
print(sol1(data, 14))


