#No.of digits count
num = int(input("Enter a number: "))
count = 0

if num == 0:
    count = 1
else:
    for i in range(1, 100):
        if num == 0:
            break
        num = num // 10
        count += 1

print("Number of digits:", count)