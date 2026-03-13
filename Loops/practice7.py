# largest of three numbers
num1 = int(input("enter the first num :"))
num2 = int(input("enter the second num :"))
num3 = int(input("enter the third num :"))
if (num1 > num3) and (num1 > num2):
    print(f"{num1} is the largest")
elif (num2 > num3) and (num2 > num1):
    print(f"{num2} is the largest")
else:
    print(f"{num3} is the largest")
