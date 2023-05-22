class Home_affairs():
    def __init__():
        pass

    def general_info(self):
        name = print('Enter your name')
        input()

        surname = print('Enter your surname')
        input()

        age = print('Enter your age')
        input()

        place = print('Where do you live')
        input()
        country = print('What is your country')
        input()

    def print_info(self):
        mo = {
            'Name':self.name,
            'Surname': self.surname,
            'Age': self.age,
            'Place': self.place,
            'Country': self.country,

        }

    def gender_cla(self):
        print('Type (m) for man or (f) for female')
        g = input()

        if g == 'm':
            ge = 'Mr'
        elif g == 'f':
            ge = 'Mrs'


class Home(Home_affairs):
    
        

    def main(self):

        mess = f'''
        Mr {self.ge}

        Hi! {self.ge.title()} {self.name} {self.surname}.You are
        our lucky winner!

        We will send your pacel in post office of {self.place}.
        We are not allowed to tell you what it is as it is a
        suprise.

        Thank you for you time.Please enjoy!

        From:
        Nivada Tech ZA
        E.Pedia
        '''
        print(mess)


ce = Home()
ce.general_info()





