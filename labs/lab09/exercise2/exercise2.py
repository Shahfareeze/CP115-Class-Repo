employee_name = input()
base_salary = int(input())
overtime_hours = int(input())
tax_status = input()

# TODO your code here

tax_rate = ""

if tax_status == "single":
    if base_salary >= 5000 :
        tax_rate = 0.22
    else :
        tax_rate = 0.18
elif tax_status == "married" :
    if base_salary >= 6000 :
        tax_rate = 0.2
    else:
        tax_rate = 0.15
elif tax_status == "head" :
    if base_salary >=5500 :
        tax_rate = 0.25
    else:
        tax_rate = 0.19

additional_deduction = 0.11 + 0.005
net_salary = base_salary + (base_salary * tax_rate) + (base_salary*additional_deduction) + (35 * overtime_hours)
        

print(employee_name)
print(f"{tax_rate}")
print(f"{net_salary:.2f}")