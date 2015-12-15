import sys, re

sum = 0
for line in sys.stdin:
    if line == '\n':
        break
    for n in re.finditer(r'-?\d+', line):
        sum += int(line[n.start():n.end()])

print(sum)