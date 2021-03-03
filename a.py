while True:
    print('enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('please enter your ager:')

while True:
    print('Please select a new passwd (alpha and number only):')
    passwd=input()
    if passwd.isalnum():
            break
    print('passwd can only include letters and numbers')
