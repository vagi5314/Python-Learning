marks = {"math":80, "science":75, "english":90}

total = 0

for subject in marks:
    total += marks[subject]

average = total / len(marks)

print("Average:", average)
