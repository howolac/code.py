import random
import sys
print("I'm thinking a number between 1 and 20.")

answer = random.randint(1, 20)
guess = None
i = 0

for guesstaken in range(1, 7):
    print('Take a gusee:')
    try:
        guess = float(input())
    except:
        print('invalid input')
        continue
    if guess < answer:
        print('Your guess is too low.')
        i = i + 1
    elif guess > answer:
        print('Your guess is too high.')
        i = i + 1
    else:
        print('Good job! You guessed my number in', i + 1, 'guesses!')
        sys.exit()

print('YOU  LOSE!', 'THE TRUE IS', int(guess), '!', guesstaken)
