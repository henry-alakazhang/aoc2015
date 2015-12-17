import sys

scene = {'children': 3,
         'cats': 7,
         'samoyeds': 2,
         'pomeranians': 3,
         'akitas': 0,
         'vizslas': 0,
         'goldfish': 5,
         'trees': 3,
         'cars': 2,
         'perfumes': 1}
         
aunt = [{} for _ in range(501)]
for line in sys.stdin:
    if line == '\n':
        break
    num = int(line.split(':')[0].split(' ')[1]) # get sue number
    parts = ''.join(line.rstrip().split(':')[1:]) # remove the 'sue #' at the start of the line
    for part in parts.split(','):
        part = part.split(' ')
        aunt[num][part[1]] = int(part[2])

        
for sue in range(1, len(aunt)):
    match = True
    for fact in iter(aunt[sue]):
        if fact == 'cats' or fact == 'trees':
            if not aunt[sue][fact] > scene[fact]:
                match = False
                break
        elif fact == 'pomeranians' or fact == 'goldfish':
            if not aunt[sue][fact] < scene[fact]:
                match = False
                break
        else:
            if not aunt[sue][fact] == scene[fact]:
                match = False
                break
    if match:
        break
        
print(sue)