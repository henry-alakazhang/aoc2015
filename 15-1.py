import itertools

#hard coded because what the heck
i = [[2,0,-2,0,3],
     [0,5,-3,0,3],
     [0,0,5,-1,8],
     [0,-1,0,5,8]]


max = 0
for a in range(101):
    for b in range(101 - a):
        for c in range(101 - a - b):
            d = 100 - a - b - c
            capacity = a * i[0][0]
            durability = b * i[1][1] + d * i[3][1]
            flavour = a * i[0][2] + b * i[1][2] + c * i[2][2]
            texture = c * i[2][3] + d * i[3][3]
            calorie = a * i[0][4] + b * i[1][4] + c * i[2][4] + d * i[3][4]
            if capacity < 0 or durability < 0 or flavour < 0 or texture < 0 or calorie != 500:
                total = 0
            else:
                total = capacity * durability * flavour * texture
            if total > max:
                max = total

print(max)