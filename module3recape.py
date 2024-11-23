#A company decided to give bonous of 5% to employee if his/her year of service is more than 5 years and salary greater then or equal 20000
# . Ask user for their salary and year of service and print the net bonus amount

salary = int(input('Enter your salary:'))
years_of_service =float(input('Enter years of service :'))

if years_of_service > 5 or salary >= 20000:
    bonus = 0.05
    net_salary = salary + salary * bonus
    print('You get net salary with bonus',net_salary,'USD')
else:
    print('You get only Main salary',salary,'USD')

