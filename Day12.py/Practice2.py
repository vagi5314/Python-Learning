def primecheck(num):
    if num % 2 != 0:
        return "prime"
    else:
        return "not prime"


num = int(input("enter the value of num :"))
print(primecheck(num))
