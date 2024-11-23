user_name = "rhwish"
password  = "owaraneed"

input_user = input('Enter User name:')
input_password = input('Enter password:')

# if input_user ==user_name and input_password==password:
#     print('You have successfully login')
# else:
#     print("user name or password might be wrong.\n Please try with correct username and password  ")
if input_user !=user_name or input_password !=password:
    print("user name or password might be wrong.\n Please try with correct username and password  ")

else:
    print('You have successfully login')