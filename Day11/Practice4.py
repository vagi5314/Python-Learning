# string reverse
string = input("enter the string : ")
rev = ""
for ch in string:
    rev = ch+rev
print(f"The reversed string is:{rev}")
