# way1
word = input("enter the word")
rev = ""
for ch in word:
    rev = ch + rev

if word == rev:
    print("Palindrome")
else:
    print("Not a palindrome")

# Another way to do it
word = input("enter the word")
# NOTE: Pyre type checker is incorrectly flagging string slicing [::-1] as an error.
# We suppress it here because slicing a string always returns a string in Python.
rev = str(word)[::-1]  # type: ignore
if word == rev:
    print("palindrome")
else:
    print("Not a palindrome")
