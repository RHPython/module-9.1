# post = {
#     'id': 100,
#     'title': 'This is awsome title',
#     'Content':'There are awesome content',
#     'author':'Awsome name',
#     'category': 'Awesome',
#     'slug':'awsome-title',
#
# }
# # post['category']='Genius'
# # post.update({'category':'Genius'})
# # post['Qualification']='CA qualified'
# post.update({'qualification':'CA qualified'})
# print(post)

car = {
    'name': 'Toyata',
    'year': 2000,
}
# car['year']='2011'
car.update({'year':2015})

print(car)
car.update({'color':'yellow'})
print(car)
print(car.get('color'))
print(car['name'])
print(car.get('year'))