import pyinputplus as pyip

# get a normal string input
# response = pyip.inputStr('normal string here pls: ')

# get a number (returns an int / float depending on what's entered)
# related = inputFloat
# response = pyip.inputNum('please enter a number: ')
# response = pyip.inputNum('please enter a valid number: ', min=4, max=6) #inclusive
# response = pyip.inputNum('please enter a valid number: ', greaterThan=4, lessThan=6) #non inclusive
# response = pyip.inputNum('please enter a valid number: ', blank=True)  # allows blank response
# max 2 attempts, 10s timeout. default sets a response in case the user hits one of the limits
# response = pyip.inputNum('please enter a valid number: ', limit=2, timeout=10, default='sorry!')
# response = pyip.inputNum('this time were allowing regexes: ',
#                          allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
# response = pyip.inputNum(
#     'this time were not accepting chetnie, but go ahead and try anyway: ', blockRegexes=[r'[02468]$'])

# user forced to select one of below
# response = pyip.inputChoice(['dog', 'cat', 'potato'])

# similar to above but actually shows the menu to the user
# response = pyip.inputMenu(['dog', 'cat', 'potato'], numbered=True)

# ensure the user enters a date
# response = pyip.inputDatetime('please enter a date in the format 2020/10/31 12:00:01: ')

# ensure user enters a yes or no response
# response = pyip.inputYesNo('please enter yes/no: ')

# takes True or False
# response = pyip.inputBool('please enter T/F: ')

# ensures inputs email
# response = pyip.inputEmail('please enter a valid email: ')

# ensure filepath, plus checks a file actually exists
# response = pyip.inputFilepath('please enter a filepath: ', mustExist=True)

# allows the user to enter password, showing * as they type
# response = pyip.inputPassword('please enter your password: ')

# we can do custom functions too


def MustAddToTen(numbers):
    L = [int(n) for n in list(numbers)]
    if sum(L) != 10:
        raise Exception('the digits must add to 10, not %s' % sum(L))
    print('good job. adds up to 10')
    return sum(L)


response = pyip.inputCustom(
    MustAddToTen, prompt='please enter numbers that add up to 10, no spaces: ')
print(response)
