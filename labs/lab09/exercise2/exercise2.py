employee_name = input("Enter your name:" )

base_salary = input("Enter your salary:" )

overtime_hours = input("Enter your overtime:")

tax_status = input("Enter your status (single/married/head):")

# TODO your code here
base_salary = float(base_salary)
overtime_hours = float(overtime_hours)

tax = ""

if tax_status == "single" and base_salary >= 5000 :
    tax = 0.22
else :
    tax = 0.18
if tax_status == "married" and base_salary >= 6000:
    tax = 0.2
else:
    tax = 0.15
if tax_status == "head"  and base_salary >=5500 :
    tax = 0.25
else:
    tax = 0.19

additional_deduction = 0.11 + 0.005
tax_rate = additional_deduction + tax
tax_salary = (base_salary * tax_rate)
overtime_salary = 35 * overtime_hours
net_salary = (base_salary - tax_salary) + overtime_salary
        

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")