price = float(input())

# TODO: Your code here
item_count=0
total_cost=0
while price != -1:
    if price >= 0 :
        total_cost+=price
    else:
        total_cost+=0
    price = float(input())


print(item_count)
print(f"{total_cost:.2f}")
