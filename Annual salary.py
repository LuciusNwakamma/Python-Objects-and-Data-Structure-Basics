print("Welcome to our company! As an employee, it is necessary to know your average annual salary")
first_name = input("Please enter your name: ")
employee_ID= input("Please enter your employee ID: ")
email = input("Please enter your email: ")
occupation = input("please enter your occupation: ")
_workdays = input("please enter your number of work days: ")
work_hours = input("Please enter your number of work hours per day: ")
hourly_wage = input("Please enter your hourly wage: ")

weekly_rate = int(hourly_wage) * int(_workdays) * int(work_hours)
gas = weekly_rate * 52
print()
print("Report summary")
print("=============================")
print("Name: " + first_name)
print("Employee ID: " + employee_ID)
print("Email: " + email)
print("Occupation: " + occupation)
print("Wage: " + hourly_wage)
print("Working " + work_hours + " hours, " + str(_workdays) + " days a week")
print(
    
    )
print("Gross Annual Salary: $" + str(gas))








