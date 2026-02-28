#Odd or Even

num = int(input("enter the value of num:"))

if(num%2==0):
    print(f"The number {num} is even")
else:
    print(f"The number {num} is odd")



#usingternary operator

num = int(input("enter the value of num:"))
print("even" if(num%2==0) else "odd")