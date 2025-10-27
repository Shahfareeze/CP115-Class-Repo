#Assignment CP
#Determine discount and calculate discounted price 

age = int(input("Input your age :"))
price = int(input("Input your price of movie ticket : "))

discount = 0
if age <= 12:
    discount = 0.5
    print ("Your discount is 50%")
elif age <= 17:
    discount = 0.25
    print("Your discount is 25%")
else :
    discount = 0
    print("No Discount")

discounted_price = price - (price * discount)
print (f"Your discounted ticket price: {discounted_price}")