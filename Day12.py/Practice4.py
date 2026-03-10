#function multiple table
def table(num):
    for i in range(1,11):
        print(num,"*",i,"=",num*i)
num = int(input("enter the value of num : "))
table(num)