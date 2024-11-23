# normal_body_temp = 98.6
# temp = float(input('Enter your body Temperature'))
#
# if temp > normal_body_temp:
#     print('Peracetamol 2 times')
# else :
#     print("vitamin tablet 3 times ")
# normal_temp =98.9
# temp = float(input("Enter body temperature : "))
# if temp > normal_temp:
#     print('paracetemol 2times daily until it in normal temperature')
# else :
#     print('Vitamin two times daily')
#Rakib Hasan is a CA in Bangladesh.He is an ACA
#Owara is a CMA in Bangladesh . She is an ACMA
name = input('Enter Name:')
gender = input('Enter Gender(m/f):')
country_name = input('Enter Country name:')
profession = input('Enter Profession :')

if gender == 'm':
    profession = 'Accountant tax'
    pronoun = 'He'
    known_as = 'ACA'
else:
    profession = 'Accountant cost'
    pronoun = 'She'
    known_as = 'ACMA'

print(f'{name}  is an {profession} in {country_name}.{pronoun} is an {known_as}')

