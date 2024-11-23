marks = int(input('Enter your mark:'))
weight= int(input('Enter your weight:'))

# if marks >= 80 or weight <= 20:
if not (marks <= 80 or weight <= 20):
    print('You will get a chocolate')
else:
    print('You get less marks and overweight ')
