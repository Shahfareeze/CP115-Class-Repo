employee_name = input("Enter your name:" )

base_salary = input("Enter your salary:" )

overtime_hours = input("Enter your overtime:")

tax_status = input("Enter your status (single/married/head):")

# TODO your code here
base_salary = float(base_salary)
overtime_hours = float(overtime_hours)

tax_rate = ""

if tax_status == "single" and base_salary >= 5000 :
    tax_rate = 0.22
else :
    tax_rate = 0.18
if tax_status == "married" and base_salary >= 6000:
    tax_rate = 0.2
else:
    tax_rate = 0.15
if tax_status == "head"  and base_salary >=5500 :
    tax_rate= 0.25
else:
    tax_rate = 0.19

additional_deduction = 0.11 + 0.005
overtime_salary = 35 * overtime_hours
total_salary = base_salary + overtime_salary
net_salary = total_salary * (1 - tax_rate) * (1 - additional_deduction)


print(employee_name)
print(f"{tax_rate * 100}%")
print(f"{net_salary:.2f}")