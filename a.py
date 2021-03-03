#！python3
#phone number found


def isPhonenum(text):
    if len(text) != 12:
        return False

    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    else:
        return True


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.415-555-9999'

for i in range(len(message) - 11):
    if isPhonenum(message[i:i + 12]):
        print('phonenumber found , it\'s ' + str(message[i:i + 12]))
print('done')