work_hours = [('z',10),('x',7),('y',12)]
def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee

        else:
            pass

    return (employee_of_month,current_max)

result = employee_check(work_hours)
print(result)

