def area_of_rectangle(length, b):
    return length*b


length = int(input("enter the length"))
breadth = int(input("enter the breadth"))
result = area_of_rectangle(length, breadth)
print(f"The area of rectangle is {result}")