import sys

lights = [[0 for i in range(0, 1000)] for j in range(0,1000)]

for line in sys.stdin:
    if (line == '\n'):
        break
    line = line.rstrip()
    words = line.split(' ')
    if (words[0] == 'turn'):
        light1 = words[2].split(',')
        light2 = words[4].split(',')
        for i in range(int(light1[0]), int(light2[0]) + 1):
            for j in range(int(light1[1]), int(light2[1]) + 1):
                if (words[1] == 'on'):
                    lights[i][j] = 1
                else:
                    lights[i][j] = 0
    elif (words[0] == 'toggle'):
        light1 = words[1].split(',')
        light2 = words[3].split(',')
        for i in range(int(light1[0]), int(light2[0]) + 1):
            for j in range(int(light1[1]), int(light2[1]) + 1):
                lights[i][j] = 1 - lights[i][j]

total = 0
for i in range(0, 1000):
    for j in range(0, 1000):
        total = total + lights[i][j]
        
print(total)