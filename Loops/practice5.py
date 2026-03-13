# Grade calculator

marks = float(input("enter the marks:"))
if (marks >= 90):
    print("A grade")
elif (marks >= 80 and marks < 90):
    print("B grade")
elif (marks >= 70 and marks < 80):
    print("C grade")
elif (marks >= 60 and marks < 70):
    print("D grade")
elif (marks >= 50 and marks < 60):
    print("E grade")
else:
    print("Fail")
