#！python3
#美国或加拿大的电话号码判断

def isPhonenum(text):
    if len(text) != 12:
        return False

    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal() :
            return False
    if text[7] != '-':
        return False
    else:
        return True


print('415-555-4242 is a phone number:')
print(isPhonenum('495-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhonenum('Moshi moshi'))
