print('Enter your name')
x = input()
print('Your Surname')
y = input()

print('Type (m) for male or (f) for female')
z = input()

if 'm':
    j = 'male'.upper()
elif 'f':
    j = 'female'.upper()

if (z == 'm'):
    print('Hello Mr ',x[0].upper(),'',y.upper())
elif (z == 'f'):
    print('Hello Mrs ',x[0].upper(),'',y.upper())

else:
    print('Please specify the gende!')

print('**** STATUS ****')
status = {
    'Name': x ,
    'Surname': y,
    'Gender':j,
}
print(status)



