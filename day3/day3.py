import sys

data = sys.stdin.readlines()
data = [e.strip() for e in data]
convert = {}

for i in range(26):
    convert[chr(97 + i)] = i + 1

for i in range(26):
    convert[chr(65 + i)] = i + 27


def rutsackComp(row):
    comp1 = row[:(len(row)//2)]
    comp2 = row[(len(row)//2):]
    lookup = set()

    for char in comp1:
        lookup.add(char)

    for char in comp2:
        if char in comp1:
            return charToPrio(char)

def charToPrio(char):
    return convert.get(char)

def sol1(data):
    sum = 0
    for row in data:
        sum += rutsackComp(row)
    
    return sum

def badgeFinder(rows):#maybe write a more generalized solution to this?
    r1,r2,r3 = rows
    lookup1 = set() #list of dictionaires potentially, make dictionairy of all r1 except last, then chain 'ands' with last element and other dictionaires
    lookup2 = set()
    for char in r1:
        lookup1.add(char)
    for char in r2:
        lookup2.add(char)

    for char in r3:
        if((char in lookup1) and (char in lookup2)):
            return charToPrio(char)
    
    

    


def sol2(data):
    sum = 0
    for i in range(0, (len(data)), 3):
        sum += badgeFinder(data[i:i+3])
    return sum

#print(sol1(data))
print(sol2(data))