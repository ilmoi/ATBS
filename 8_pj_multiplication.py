# pose 10 multiplication problems to the user
import pyinputplus as pyip
import random
import time

numberOfQuestion = 10
correctAnswers = 0

for i in range(numberOfQuestion):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    result = x*y

    print(f'what is {x} times {y}?')
    print('youve got 3 attempts and 30s!')

    try:
        pyip.inputStr('please enter your response: ', blockRegexes=[(
            r'.*', 'incorrect input')],
            allowRegexes=[r'^%s$' % result],
            limit=3, timeout=30)
    except pyip.TimeoutException:
        print('out of time!')
    except pyip.RetryLimitException:
        print('out of tries!')
    else:
        correctAnswers += 1
        print('congrats you got it right!')

time.sleep(1)
print(f'your total score is {correctAnswers} our of 10!')
