import nanoid
class Home():
    def __init__(self):
        self.name = input('Name: ')
        self.surname = input('Surname: ')
        self.age = input('Age: ')
        self.place = input('Place: ')


    def gender(self):
        print('Type (m) for male or (f) for female.')
        zone = input()

        if zone == 'm':
            genderType = 'Mr. '
        elif zone == 'f':
            genderType = 'Mrs.'
        else:
            genderType = 'Mr/Mrs '


            
            
        mess = f'''
        {genderType} {self.name[0].upper()} {self.surname.title()}

        HI! {self.name.title()} {self.surname.title()} living at {self.place} .We like to inform you
        about our next system update at Nivada inc.

        On 20 May 2023 we will be updating our system from version 1.26 to
        version 1.27 which comes with the latest security shield.You are 
        advised to switch to the new version when it commense.

        Thank you for your time!Have a good day.

        Nivada Tech Inc
        USA,Ioa
        
        '''
        print(mess)
        

class Data(Home):
    def __init__(self):
        super().__init__()

    def engine_v1(self):
        print('******* NIVADA *****')
        #gender()
        #nano()

class Play(Home):
    def __init__():
        super().__init__()

    def angel(self):
        print('My name is ',self.name)
        print(f'I have {self.age} living at {self.place}')

class Man(Home):
    def mama(self):
        print(self.name)
        print(f'My surname is {self.surname}')
        print(f'Living at {self.place}')

class Validate(Play,Home):
    def __init__():
        super().__init__()

    def moon(self):
        print(f'My name is {self.name}')

class Fail(Man,Home):
    def joe(self):
        print(f'My name is {self.name}')

zen = Fail()
zen.joe()


    

zen.gender()

class generate_qr():
    def __init__(self,*args,**kwaargs):
        return None

    def qr_fun(self):  # function that generate qr 5-digits number
        code = nanoid.generate()
        first_code = code[0:2]
        last_code = code[-3:-1]
        middle_code = code[10]
        qr_5_digit_no = first_code + middle_code + last_code
        return qr_5_digit_no
        

