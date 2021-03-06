#！python3
#正则表达式
#匹配短句
import re, pyperclip

regex = re.compile(
    r'((alice|Bob|carol)\s(eats|pets|throws)\s(apple|cats|baseball))',
    re.IGNORECASE)
print(
    regex.findall('''
 'Alice eats apples.'
 'Bob pets cats.'
 'Carol throws baseballs.'
 'Alice throws Apples.'
 'BOB EATS CATS.'
但不匹配：
 'RoboCop eats apples.'
 'ALICE THROWS FOOTBALLS.'
 'Carol eats 7 cats.'
'''))
