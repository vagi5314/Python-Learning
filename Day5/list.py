# list and its methods
list1 = [56, 76, 89, 75, 13, 12, 90, 45]
list2 = [34, 67, 59, 43, 38, 93, 27, 73]

print(len(list1+list2))
list3 = list1.extend(list2)
print(list3)


list1.append(100)
print(list1)
list1.remove(56)
print(list1)


list2.sort()
print(list2)
list2.reverse()
print(list2)


print(list2[0])
print(list2[-1])
print(list2[2:5])


print(min(list2))
print(max(list1+list2))

print(list1.count(56))

print(list1.index(56))

list1.insert(2, 100)
print(list1)
