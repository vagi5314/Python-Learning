# largest number
def largest(a, b, c):
    if a > b and a > c:
        return a, "is largest"
    elif b > a and b > c:
        return b, "is largest"
    else:
        return c, "is largest"


a = int(input("enter the value of a : "))
b = int(input("enter the value of b : "))
c = int(input("enter the value of c : "))
print(largest(a, b, c))
