import re, sys

nice = []
naught = []

for word in sys.stdin:
    if (word == '\n'):
        break
    if re.search(r'.*[aeiou].*[aeiou].*[aeiou].*', word) != None:
        print("ok1")
        if re.search(r'(\w)\1', word) != None:
            print("ok2")
            if re.search(r'ab|cd|pq|xy', word) == None:
                nice.append(word)
                
print(len(nice))