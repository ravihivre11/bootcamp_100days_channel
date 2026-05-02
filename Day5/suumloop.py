marks = [23,65,32,1,23,43,21]
print(sum(marks))

sum = 0
for mark in marks:
    sum += mark
print(sum)

max = 0
for mark in marks:
    if mark > max:
        max = mark
print(max)