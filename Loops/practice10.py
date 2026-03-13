# multiplication table of a number
num = int(input("enter the value of num:"))
for i in range(1, 17):
    print(i, "*", num, "=", num*i)


# Using while loop
i = 1
while (i <= 16):
    print(i, "*", num, "=", num*i)
    i += 1
