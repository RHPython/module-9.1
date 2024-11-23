user= {
    'id':900405,
    'first_name': 'Rakib',
    'last_name':'Hasan',
    'Level_Complete': 'Certificate Level',
    'username':'rhwish',
    'password':'900405',
    'role':'student',
}
# level_complete = user['Level_Complete']
# print(level_complete)
level_complete = user.get('Level_Complete')
print(level_complete)