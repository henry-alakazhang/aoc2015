import re

def isValid(password):
    ok = False
    for i in range(0, len(password)-2):
        if ord(password[i+1]) == ord(password[i]) + 1:
            if ord(password[i+2]) == ord(password[i]) + 2:
                ok = True
                break
    if 'l' in password or 'i' in password or 'o' in password:
        ok = False
    if not re.search(r'(.)\1.*([^\1])\2', password):
        ok = False
    return ok

def next(word):
    last = word[len(word)-1]
    if (last == 'z'):
        if (len(word) == 1):
            return 'z'
        start = next(word[0:len(word)-1])
        return start + 'a'
    else:
        start = word[0:len(word)-1]
        return start + chr(ord(last) + 1)
        
old = 'hxbxwxba'

for _ in range(2):
    new = next(old)
    while not isValid(new):
        new = next(new)
    print(new)
    old = new
