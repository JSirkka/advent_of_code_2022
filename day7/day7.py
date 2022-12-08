import sys

data = sys.stdin.readlines()


dirs = {}
history = ['']

size_dic = {}

for line in data:

    line = line.split(' ')
    
    if line[0] == '$':
        if line[1] == 'cd':
            dir_name = line[2].strip()
            if dir_name == '..':
                history.pop(-1)
            else:
                path = history[-1] + dir_name
                history.append(path)
                if path not in dirs.keys():
                    dirs[path] = []
    
    if line[0] == 'dir':
        dirs[history[-1]].append(history[-1] + line[1].strip())

    if line[0].isdigit():
        dirs[history[-1]].append(line[0].strip())


def dir_size(dir):
    size = 0
    stack = [dir]

    while(len(stack) > 0):
        current_dir = stack.pop()
        items = dirs[current_dir]

        for ite in items:
            if ite.isdigit():
                size += int(ite)
            else:
                if(ite in size_dic.keys()):
                    print('this happens')
                    size += size_dic[ite]
                else:
                    stack.append(ite)
        

    return size
    

def sol1():
    summe = 0
    for dir in dirs.keys():
        size = size_dic.get(dir)
        if size <= 100000:
            summe += size

    return summe

for dir in dirs.keys():
    size_dic[dir] = dir_size(dir) 

print(sol1())


def sol2():
    total_space = 70000000
    update = 30000000
    unused_space = total_space - size_dic['/']
    space_needed = update - unused_space
    
    candidates = []
    for size in size_dic.values():
        left = size - space_needed
        if(left >= 0): #this can be better optimized, but didnt work with first solotion for some reason
            candidates.append(size)
        
    
    return min(candidates)

    
print(sol2())