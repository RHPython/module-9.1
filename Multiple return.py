def multiple_return (a,b):
    add = a+b
    subs = a-b
    mult =a*b
    return add,subs,mult
x,y,z = multiple_return(5,2,)
print(z)
print(y)