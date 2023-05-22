# 

class General_Info():
    def __init__(self,usr_name = input('User Name: '),pass_word = input('Password: ')):

        self.usr_name = usr_name
        self.pass_word = pass_word

        database = []

    def validate(self):
        if self.usr_name in database:
            print('...OK!...')
        else:
            print('Your username does not match any on the database')
            print('If you have acount,try again')


    def pass_verify(self):
        if self.pass_word in database:
            print('Password Accepted')
        else:
            print('Password Denied!')
            print('Try Again .....')

    def nano(self):
        pass


class Login(General_Info):
    def loggin(self):
        print('Are you a member or Admin (Type "M" for member or "A" for admin')
        var = input()

        if var == 'A' or 'a':
            print('Enter your Admin code')
            code = input()
            
            if code in database:
                print('...OK!...')
                print('Let get our hands busy..do not be lazy')

            else:
                print('..Invalid Code entered!..')
                print('..We suggest you try again..')

        elif var == 'M' or 'm':
            print('Welcome back member')

        else:
            print('Please specify your position above')


logging = True

while logging:
    return play()
else:
    za.loggin()
