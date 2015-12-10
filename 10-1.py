c = '1321131112'

for _ in range(50):
    new_c = ''
    i = 0
    while i < len(c):
        step = 0
        while c[i+step] == c[i]:
            step += 1
            if i+step >= len(c):
                break
        new_c += str(step)
        new_c += str(c[i])
        i += step
    c = new_c
    
print(len(c))