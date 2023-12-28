user={
    'username':'Akram',
    'password':'akram123'
    }
username=input('Enter the usename.....:')
password=input('Enter the password.... :')
if username!=user['username']:
    print('username is invalid')
else:
    print('username is valid')
if password!=user['password']:
    print('password is incorrect')
else:
    print('password is valid')


