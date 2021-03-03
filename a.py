#！python3
''' 
一个口令小脚本

'''

import sys, pyperclip

passwd = {
    'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
    'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
    'luggage': '12345'
}

if len(sys.argv) < 2:
    print('Usage: python a.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in passwd:
    print('the passwd is' + ' ' + passwd[account])
    pyperclip.copy(passwd[account])
    print('the account' 'is' + ' ' + account)

else:
    print('not match')
