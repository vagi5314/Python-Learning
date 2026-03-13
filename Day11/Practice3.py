# count vowels in a word
word = input("enter the word : ")
vowels = "aeiouAEIOU"
count: int = 0
for ch in vowels:
    if ch in word:
        # NOTE: Pyre incorrectly flags `+=` as missing a `__add__` overload for integers
        count += 1  # type: ignore
print(count)
