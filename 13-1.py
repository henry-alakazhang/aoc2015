import sys, itertools

people = ['Me']
happy = {'Me':{}}

for line in sys.stdin:
    if line == '\n':
        break
    words = line.rstrip().split('.')[0].split(' ')
    if words[0] not in people:
        people.append(words[0])
        happy[words[0]] = {}
        happy[words[0]]['Me'] = 0
        happy['Me'][words[0]] = 0
    if words[10] not in people:
        people.append(words[10])
        happy[words[10]] = {}
        happy[words[10]]['Me'] = 0
        happy['Me'][words[10]] = 0
    if words[2] == 'gain':
        happy[words[0]][words[10]] = int(words[3])
    else:
        happy[words[0]][words[10]] = -int(words[3])
    
max = ((), -2**32+1)  
for perm in itertools.permutations(people):
    sum = 0
    for i in range(0, len(perm)-1):
        sum += happy[perm[i]][perm[i+1]]
        sum += happy[perm[i+1]][perm[i]]
    # then round the table
    sum += happy[perm[0]][perm[len(perm)-1]]
    sum += happy[perm[len(perm)-1]][perm[0]]
    if sum > max[1]:
        max = (perm, sum)
    
print(max)