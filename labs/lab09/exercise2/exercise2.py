employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

# TODO your code here


tax_rate = ""
if tax_status == "Single":
    if base_salary >= 5000 :
        tax_rate = 0.22
    else:
        tax_rate = 0.18
elif tax_status == "Married" :
    if base_salary >= 6000:
        tax_rate = 0.2
    else:
        tax_rate = 0.15
elif tax_status == "Head":
    if base_salary >=5500 :
        tax_rate = 0.25
    else:
        tax_rate = 0.19



overtime_salary = 35 * overtime_hours
total_salary = base_salary + overtime_salary
net_salary = total_salary * (1-tax_rate) * (1 - 0.115)


print(employee_name)
print(f"{tax_rate * 100:.0f}%")
print(f"{net_salary:.2f}")