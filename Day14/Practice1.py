import sys
my_list = [70, 77, 89, 10, 90]
largest = second_largest = -sys.maxsize - 1
for i in my_list:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print(largest)
print(second_largest)
