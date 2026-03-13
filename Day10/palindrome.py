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
rev = str(word)[::-1]
if word == rev:
    print("palindrome")
else:
    print("Not a palindrome")
