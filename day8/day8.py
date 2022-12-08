import sys

data = sys.stdin.readlines()

matrix = [[int(n) for n in a.strip()] for a in data]

def visible(i,j):

    row = matrix[i]
    col = []

    for ele in matrix:
        col.append(ele[j])

    surrounding = []
    surrounding.append(row[:j])
    surrounding.append(row[j+1:])
    surrounding.append(col[:i])
    surrounding.append(col[i+1:])
    
    for dir in surrounding:
        if not dir or matrix[i][j] > max(dir):
            return True

    return False

def sol1():
    count = len(matrix)*2 + len(matrix[0])*2 - 4
    count = 0
    for i in range(len(matrix)):
        visual = ""
        for j in range(len(matrix[0])):
            if visible(i, j):
                visual += "@"
                count += 1
            else:
                visual += "."
        print(visual)

    return count

def scenic_score(i,j):
    row = matrix[i]
    col = []

    for ele in matrix:
        col.append(ele[j])

    surrounding = []
    surrounding.append(row[:j][::-1])
    surrounding.append(row[j+1:])
    surrounding.append(col[:i][::-1])
    surrounding.append(col[i+1:])

    counts = 1
    for dir in surrounding:
        count = 0
        for tree in dir:
            if tree >= matrix[i][j]:
                count += 1
                break
            
            count += 1
        counts *= count    
    
    return counts
            
def sol2():
    best = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            score = scenic_score(i, j)
            if score > best:
                best = score

    return best



print(sol1())
print(sol2())