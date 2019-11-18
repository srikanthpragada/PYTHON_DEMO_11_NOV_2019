# Print average of positive numbers
count = total = 0

for i in range(10):
    num = int(input('Enter a number :'))
    if num == 0:
        break

    # Ignore negative numbers
    if num < 0:
        continue

    total += num
    count += 1

print("Average : ", total // count)




