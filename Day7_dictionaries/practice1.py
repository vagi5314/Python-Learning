marks = {"math":80,"science":75,"english":90}
for i in marks:
    print(i,marks[i])
print(marks.values())
marks["history"] = 74
print(marks)
marks.pop("math")
print(marks)