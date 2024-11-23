person_one = ['Morish','male','australia','29th January 1998','moris@jon.com','01-0716-1221']
person_two = ['Vasco','male','ukrain','29th oct 1998','vasco@jon.com','01-0716-1221']

person = [
    ['Morish','male','australia','29th January 1998','moris@jon.com','01-0716-1221'],
    ['Vasco','male','ukrain','29th oct 1998','vasco@jon.com','01-0716-1221'],
    ['fasco','male','England','29th oct 1998','vasco@jon.com','01-0716-1221'],
    ['masco','male','Argentina','29th oct 1998','vasco@jon.com','01-0716-1221'],
    ['Dasco','male','India','29th oct 1998','vasco@jon.com','01-0716-1221']
]
i = 0
while i < len(person):
    single_person = person[i]
    name = single_person[0]
    gender = single_person[1]
    country = single_person[2]
    bith_date = single_person[3]
    email = single_person[4]
    if gender == 'male':
        pronoun ='he'
        relative = 'his'
    else:
        pronoun = 'she'
        relative ='her'
    sentence = f'{name.title()} lives in {country}.{pronoun.title()} was born in {bith_date}.{relative} email address is {email}.'
    # print(name,gender,country,email,sep="----")
    print(sentence)
    i = i + 1