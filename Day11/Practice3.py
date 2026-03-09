word = input("enter the word : ")
vowels = "aeiouAEIOU"
count=0
for ch in vowels:
    if ch in word:
        count+=1
print(count)
