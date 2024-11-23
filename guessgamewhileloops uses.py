import random
number = [1,2,3,4,5,6,7,8,9]

print('Games Start and Guess a number form 1-9')
print('*'*40)
computer_number = random.choice(number)
while True :
    number = int(input('What is your guess: '))
    if computer_number == number:
       print('Contratulations')
       break
    else:
       print('Hoy Nai')