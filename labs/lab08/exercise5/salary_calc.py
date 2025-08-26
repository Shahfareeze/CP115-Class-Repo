import employee_data

deduction_EPF = 0.11
deduction_SOCSO = 0.005
deduction_EIS = 0.002

total_salary =  employee_data.basic_salary + (employee_data.overtime_hours * employee_data.overtime_rate)

total_deduction = deduction_EIS + deduction_SOCSO + deduction_EPF

final_salary = total_salary * total_deduction