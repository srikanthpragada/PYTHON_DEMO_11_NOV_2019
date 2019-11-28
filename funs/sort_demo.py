def abs(n):
    return n if n >= 0 else n * -1


nums = [-10, 20, 30, -50, -90, -2]

for n in sorted(nums, key=abs):
    print(n)
