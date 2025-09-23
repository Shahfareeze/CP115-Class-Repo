position = input()
overtime_hours = int(input())
is_weekend = input()

# Your code here

base_hourly_rate = 0
hourly_rate = 0
overtime_pay = 0
total_pay = 0


if position == "Manager":
    base_hourly_rate = 35 
    
elif position == "Supervisor":
    base_hourly_rate = 25
    
elif position == "Staff":
    base_hourly_rate = 18
    



bonus_weekend = 0

if is_weekend == "Yes" :
    bonus_weekend_pay =  (overtime_hours * 5)
elif is_weekend == "No":
    bonus_weekend_pay = 0

hourly_rate = base_hourly_rate
overtime_pay = ((overtime_hours * base_hourly_rate) * 1.5 )+ bonus_weekend_pay
total_pay = overtime_pay 

print(hourly_rate)
print(overtime_pay)
print(total_pay)