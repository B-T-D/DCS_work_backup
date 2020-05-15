
def password():
    username = input('Username: ')
    password = input('Password: ')
    return username == 'alan.turing' and password == 'notTouring'

print(password())
