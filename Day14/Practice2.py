import sys
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
smallest = second_smallest = sys.maxsize
for i in my_list:
    if i < smallest:
        second_smallest = smallest
        smallest = i
    elif i < second_smallest and i != smallest:
        second_smallest = i
print(smallest, second_smallest)
