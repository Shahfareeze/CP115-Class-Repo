principal = float(input())
rate = float(input())
time = float(input())
interest = principal * rate * time
print(interest)
totalAmount = interest + principal
print(totalAmount)
monthlyInterest = interest / time * 12
print(monthlyInterest)
