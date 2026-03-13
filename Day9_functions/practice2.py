# function for even orodd
def oddeven():
    num = int(input("enter the value of num:"))
    if num % 2 != 0:
        print(num, "is odd")
    else:
        print(num, "is even")


oddeven()
