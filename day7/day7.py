import sys

data = sys.stdin.readlines()

class Folder:
    children = []
    files = []
    
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
    
    def add_size(n):
        size += n

    def add_children(child):
        children.append(child)


folders = []

folders.append(Folder('/', None))
last_dir = folders[0]

for line in data:

    line = line.split(' ')
    
    if line[0] == '$':
        if line[1] == 'cd':
            dir_name = line[2].strip()
            if dir_name == '..':
                last_dir = last_dir.parent
            else:
                new_dir = (Folder(dir_name, last_dir))
                last_dir.add_children(new_dir)
                last_dir = new_dir
        
    if line[0] == 'dir':
        pass

        
#Maybe do this in java

for e in folders:
    print(e.name, e.parent)
    