person_one = ['Morish','male','australia','29th January 1998','moris@jon.com','01-0716-1221']

person_two = ['Vasco','male','ukrain','29th oct 1998','vasco@jon.com','01-0716-1221']

gender = person_one[1]
if gender == 'male':
    relative= 'his'
    pronoun ='he'
else :
    relative = 'her'
    pronoun = 'she'
sentence = f'{person_one[0]} in {person_one[2].title()}. His date of bith is {person_one[3]}.{pronoun.title()} is avaliable at {person_one[4]} and phone no is{person_one[-1]}'

print(sentence)
