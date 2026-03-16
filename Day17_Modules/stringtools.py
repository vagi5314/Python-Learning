def count_vowels(word):
    
    vowels = "aeiouAEIOU"
    count = 0
    for i in word:
        if i in vowels:
            count+=1
    return count
    

def reverse(word):
    
    rev = ""
    for i in word:
        rev = i+rev
    return rev

def palindrome(word):
    
    rev = word[::-1]
    if word == rev:
        return True
    else:
        return False



    