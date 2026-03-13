# Tuple and its methods

my_tuple: tuple[int, ...] = (5, 10, 15, 20, 25, 30)
print(my_tuple[0:4])  # type: ignore
print(my_tuple[-1:-4:-1])  # type: ignore
print(my_tuple[0::2])  # type: ignore
