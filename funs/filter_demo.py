def iseven(n):
    return n % 2 == 0


nums = [11, 10, 30, 45, 67, 80]

for n in filter(iseven, nums):
    print(n)

