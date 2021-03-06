#！python3
#正则表达式

import re, pyperclip

emailregext = re.compile(
    r'''(
[a-zA-Z0-9._%+]+ #username
@   #@ symbol
[0-9a-zA-Z.-]+ #domain name
(\.[a-zA-Z]{2,4}) #dot-something

)''', re.VERBOSE)

emailmatch = []
text = str(pyperclip.paste())

for i in emailregext.findall(text):
    emailmatch.append(i[0])

phoneamtch = []
phontregext = re.compile(
    r'''(
(\d{3}|\(\d{3}\))? #area code
(\s|-|\.)?                 #separator|
(\d{3})                  #first 3 digits
(\.|-|\s)    # separator
(\d{4})     #last 4 digits
(\s*(ext|x|ext.)\s*\d{3,5})?        #extension

)''', re.VERBOSE)

for i in phontregext.findall(text):
    phoneamtch.append(i[0])

#这里简化只写一个
if len(emailmatch) > 0:
    pyperclip.copy('\n'.join(emailmatch) + ''.join(phoneamtch))
    print('emails:')
    print('\n'.join(emailmatch))
    print('phonenums:')
    print('\n'.join(phoneamtch))
else:
    print('no email match at least')
