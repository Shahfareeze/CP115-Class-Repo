# DESCRIBE EVERY VARIABLE CORRECTLY and FINAl ANSWER MUST 24

friends = 6
main_dishes = 25
appetizers = 12
drinks = 8

order_main_dishes = 3
order_appetizers = 2
order_drinks = 4

total_main_dishes = order_main_dishes * main_dishes
total_appetizers = order_appetizers * appetizers
total_drinks = order_drinks * drinks

service_tax = 0.1
delivery_fee = 5

total_bill = (total_main_dishes + total_appetizers + total_drinks)
final_total = ((total_bill * service_tax) + total_bill) + delivery_fee
print(total_appetizers)
print(total_drinks)
print(total_main_dishes)
print(total_bill)

split_bill = (final_total // friends)
print(f"Split bill = {split_bill}")