import hashlib

KEY = "bgvyzdsv"

for i in range(0,10000000):
    msg = KEY + str(i)
    hash = hashlib.md5(msg.encode('UTF-8')).hexdigest()
    if (hash[0:5] == "00000"):
        print(i)
        break