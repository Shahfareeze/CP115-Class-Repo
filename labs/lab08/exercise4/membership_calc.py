base_membership = 120
personal_training_cost = 80
booking_session = 6

locker_rental = 25
towel_service = 15
#This only for the new member
one_time_registration_fee = 50 

total_personal_training_cost = personal_training_cost * booking_session
total_first_month = base_membership + one_time_registration_fee + total_personal_training_cost + locker_rental + towel_service

total_monthly_cost = base_membership + total_personal_training_cost + locker_rental + towel_service

total_annual_cost = total_first_month + (total_monthly_cost * 11)

print(f"Total first month cost= {total_first_month}")
print(f"Total monthly cost = {total_monthly_cost}")
print(f"Total annual cost = {total_annual_cost}")