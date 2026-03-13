# palindrome function
def palindrome(word):
    rev = ""
    for i in word:
        rev = i+rev
    if (word == rev):
        print("palindrome")
    else:
        print("not a palindrome")
    return rev


new = palindrome(word=input("enter the word : "))
print(new)
