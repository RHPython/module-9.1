
users =[
{
    'username':'anata',
    'password':'jolil',
    'role': 'Admin'
},
{
    'username': 'Shakib',
    'password': 'pass',
    'role': 'Co_Admin'
},
]
for user in users:
    print(user.get('username'))