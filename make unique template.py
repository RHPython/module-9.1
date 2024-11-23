import random

person = ['Moris','Chitagong']
name = person[0]
location = person[1]

sentence_one_group =[
    f'This is {name}',
    f'Mynameis {name}',
    f'{name} is my name',
]

sentence_one = random.choice(sentence_one_group)
# print(sentence_one)

sentence_two_group = [
    f'I live in {location}' ,
    f'I reside in {location}',
    f'I was raised in {location}',
    f'{location}is place where i reside',
]
sentence_two = random.choice(sentence_two_group)
pragraph= f'{sentence_one}.{sentence_two}'
print(pragraph)