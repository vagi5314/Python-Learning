#Reverse a number
num = int(input("Enter a number: "))
reverse = 0

for i in range(100):
    if num == 0:
        break
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)