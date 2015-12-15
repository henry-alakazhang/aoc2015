import sys

TIME_MAX = 2503

# 2d array of reinder to speed-time-rest-travelled-wins
reindeer = []

for line in sys.stdin:
    if line == '\n':
        break
    words = line.rstrip().split(' ')
    reindeer.append([int(words[3]),int(words[6]),int(words[13]),0,0])

for i in range(TIME_MAX):
    for deer in reindeer:
        if i % (deer[1] + deer[2]) < deer[1]:
            deer[3] += deer[0]
    
    max = 0
    for deer in reindeer:
        if deer[3] > max:
            max = deer[3]
    
    for d in range(0, len(reindeer)):
        if reindeer[d][3] == max:
            reindeer[d][4] += 1

max = 0            
for d in reindeer:
    if d[4] > max:
        max = d[4]

print(reindeer)
print(max)