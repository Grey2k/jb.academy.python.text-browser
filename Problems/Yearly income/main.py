# write your code here
year_salaries = []

with open('salary.txt', 'r') as monthly:
    for line in monthly:
        year_salaries.append(int(line) * 12)

with open('salary_year.txt', 'w') as year_salary:
    for line in year_salaries:
        print(line, file=year_salary)
