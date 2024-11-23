# print('I\'m \na ACA')
number = 5
guess = int(input('Enter Your Number'))
# if guess == number:
#     print('You are qualified accounted')
# # expected an indented block means not using tab
# elif guess > number:
#     print('You are not qualified .\n please try again... ')
# else:
#     print("'He\'s exam result is passed.\n One subject remain.")

if guess != number:
    if guess > number:
        print('You have entered larger number')
    else:
        print('You have entered smaller number')
else:
    print('You Have won the game')