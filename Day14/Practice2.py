list = [1,2,3,4,5,6,7,8,9,10]
smallest=second_smallest=float('inf')
for i in list:
    if i<smallest:
        second_smallest = smallest
        smallest = i
    elif i>smallest and i<second_smallest:
        second_smallest = i
print(smallest,second_smallest)