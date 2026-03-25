# wordcount in a sentence
sentence = input("enter the sentence : ")
count = 0
for i in sentence:
    if i == " ":
        count += 1
print(count + 1)

# or you can use this

print(len(sentence.split()))
