grade = float(input())

# TODO: Your code here
valid_count = 0
average = 0
total_grade = 0
while grade != -1:
    if grade >= 0:
        if grade <=100:
            valid_count += 1
            total_grade += grade
        else:
            valid_count+=0
    else:
        valid_count += 0 

    grade = float(input())

average = total_grade/valid_count

print(valid_count)
print(f"{average:.2f}")
