user_one = ['Owara',22,False,'andaman']
#             0         1    2       3
#            -4        -3   -2      -1

# print(type(user_one))
# print(len(user_one))
# print(user_one[0],user_one[-4],sep='--------')
# print(user_one[1],user_one[-3],sep='--------')
# print(user_one[3] ,user_one[-1],sep='--------')
#
# partial_list = user_one[1:3]
# print(partial_list)

# John Doa is a man of 26 years old . he lives in kamruk kamakha
name = user_one[0]
age = user_one [1]
living_place = user_one[3]
is_male = user_one[2]
if is_male:
    pronoun ='He'
    gender = 'man'
else:
    pronoun = 'she'
    gender = 'woman'

sentence = f'{name} is a {gender} of {age} years old . {pronoun} lives in {living_place}.'
print(sentence)
