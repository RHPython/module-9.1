number = int(input('Enter Number:'))


# if number >= 80:
#     if number < 100:
#         print('A+')
#     else:
#         print('Invalid Number has beem input')
# elif number >= 70:
#     print('A')
# else :
#     print('Failed')

# and is an operator

if number >= 80 and number <= 100:
    print('A+')

elif number >= 70 and number <= 79:
    print('A')
elif number< 69 and number>=0:
    print("you have failed")
else:
    print('Invalid Number')