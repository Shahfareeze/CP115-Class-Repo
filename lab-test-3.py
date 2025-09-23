#Shahfareeze bin Ramlee

"""
asks the user to enter the monthly usage and 
then calculates and displays the amount of the bill 
to be paid after receiving the discount
"""
usage = int(input("Enter you usage :" ))

discount = 0

#Selection Control Structur for get discount

if usage < 50 :
    discount = 1
elif usage <= 100:
    discount = 0.95
elif usage > 100:
    discount = 0.80

amount_bill = usage * discount

print(f"Your amount of the bill is {amount_bill}")



