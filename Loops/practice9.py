#Even numbers from 1 to 100 Approach1

for i in range(1,101):
    if(i%2==0):
        print(i, end=" ")


#Approach 2
for i in range(2,101,2):
    print(i, end=" ")


#Using while loop Approach 2
i = 2
while(i<=100):
    print(i, end=" ")
    i+=2    