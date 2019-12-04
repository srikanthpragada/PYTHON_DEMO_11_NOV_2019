i = 1
sum = 0
while i <= 5:
    try:
        num = int(input("Enter a number :"))
        sum += num
        i += 1
    except:
        pass

print("Sum = ", sum)
