import re


def stripz(string, char=' '):
    # make sure escape characters work ok
    if char in '.^$*+?{}[]\|()':
        char = '\\'+char
    r_front = re.compile(r'^(%s)+' % char)
    r_back = re.compile(r'(%s)+$' % char)
    string = r_front.sub('', string)
    string = r_back.sub('', string)
    print(string)


stripz('aaaabaaaaa', 'a')
stripz('..b..', '.')
stripz('???b???', '?')
