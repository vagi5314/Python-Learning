# wordcount in a sentence
sentence = input("enter the sentence : ")
count: int = 0
for i in sentence:
    if i == " ":
        count += 1  # type: ignore
print(count + 1)  # type: ignore

# or you can use this

print(len(sentence.split()))
