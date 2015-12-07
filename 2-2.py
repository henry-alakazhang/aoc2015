import sys

total = 0
for line in sys.stdin:
    if line == '\n':
        break
    line.rstrip('\n')
    nums = line.split('x')
    nums[0] = int(nums[0])
    nums[1] = int(nums[1])
    nums[2] = int(nums[2])
    nums.sort()
    per = 2* (int(nums[0]) + int(nums[1]))
    vol = int(nums[0]) * int(nums[1]) * int(nums[2])
    total = total + per + vol
    
print(total)