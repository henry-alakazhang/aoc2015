import sys

total = 0
for line in sys.stdin:
    if line == '\n':
        break
    nums = line.split('x')
    mult1 = int(nums[0]) * int(nums[1])
    min = mult1
    mult2 = int (nums[1]) * int(nums[2])
    min = mult2 if (min > mult2) else min
    mult3 = int(nums[2]) * int(nums[0])
    min = mult3 if (min > mult3) else min
    total = total + 2*mult1 + 2*mult2 + 2*mult3 + min
    
print(total)