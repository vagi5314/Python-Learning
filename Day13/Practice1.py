def largest():
    numbers = input("enter the numbers with spaces : ")
    num = numbers.split()
    new_numbers = list(map(int, num))
    print(max(new_numbers))


largest()
