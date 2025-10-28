number = float(input())

# TODO: Your code here
positive_count = 0
positive_sum = 0 

while number != 0:
    if number > 0:
        positive_count += 1
        positive_sum += number
        number = float(input())
    else:
        number = float(input())



print(positive_count)
print(f"{positive_sum:.2f}")
