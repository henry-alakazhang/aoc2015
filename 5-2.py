import re, sys

nice = []
naught = []

for word in sys.stdin:
    if (word == '\n'):
        break
    if re.search(r'(..).*\1', word) != None:
        if re.search(r'(.).\1', word) != None:
            nice.append(word)
                
print(len(nice))