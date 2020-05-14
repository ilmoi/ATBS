import re

# create a regex object using a RAW (r) string
phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# run a search (searches entire string) using .search() to return a Match Object (mo)
mo = phone_regex.search('my number is 415-535-5899')
# print out what it found using .group()
try:
    print(mo.group())
except:
    print('phone number not found')


print('-'*100)
# we can breakdown our raw string into more groups to be searched using ()
phone_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_regex.search('my number is 415-535-5899')
print(mo.group(1))
print(mo.group(2))
# print(mo.group(3)) # expecting an error
print(mo.group(0))
print(mo.group())
print(mo.groups())  # returns all groups together


# in regex the following characters have special meaning (and need to be escaped): .  ^  $  *  +  ?  {  }  [  ]  \  |  (  )


print('-'*100)
# we can search for multiple groups simultaneously using the pipe |
phone_regex = re.compile(r'batman|tina fey')
mo = phone_regex.search('two people showed up - batman and tina fey')
print(mo.group())  # only finds th first


print('-'*100)
# we can search for multiple patterns using with parts repeating
r = re.compile(r'bat(mobile|copter|man)')
mo = r.search('batman batmobile')
print(mo.group())  # prints the entire thing
print(mo.group(1))  # prints only the inside of brackets that was matched


print('-'*100)
# we can mark certain parts of the search as optional. NOTE: we need to put ? at the end of the optional part, and have that part in brackets
r = re.compile(r'bat(wo)?man')
mo = r.search('batman')
print(mo.group())
mo = r.search('batwoman')
print(mo.group())


print('-'*100)
# we can mark a certain part to appear as many times as necessary (starting with 0) with the *. NOTE: + requires at least one match
r = re.compile(r'(dino)*saur(us)*')
mo = r.search('dinosaur')
print(mo.group())
mo = r.search('dinodinodinodinosaur')
print(mo.group())
mo = r.search('saur')
print(mo.group())
mo = r.search('dinodinosaurususus')
print(mo.group())
r = re.compile(r'(dino)*saur(us)+')
mo = r.search('dinosaur')
try:
    print(mo.group())
except:
    print('no match!')

# thus
# ? = match 0 to 1
# * = match 0 to many
# + = match 1 to many


print('-'*100)
# we can use braces to specify how many times we want the expression to appear
# Ha{3} = 3 times
# Ha{3,5} = from 3 to 5
# Ha{3,} = 3 or more
# Ha{,5} = 5 or fewer
# NOTE: you need to have () around the repeating expression!
# NOTE: python expressions are greedy by default. To return non-greedy version, add a question mark at the end: {3,5}?
r = re.compile(r'(Ha){3,5}')
mo = r.search('HaHaHa')
print(mo.group())
mo = r.search('HaHaHaHaHa')
print(mo.group())


print('-'*100)
# we can find many matches using .findall() instead of .search()
# NOTE: as long as no groups are involved, returns a string not a group object
r = re.compile(r'\d\d\d')
mo = r.findall('this string has two numbers: 123 and 456')
print(mo)
# if groups are involved - wil return tuples with groups
r = re.compile(r'(\d\d)-(\d\d\d)')
mo = r.findall('this string has 4 groups: 12-123 and 45-456')
print(mo)


# more character classess:
# \d = digit
# \D = all else
# \w = digit, word, underscrore (word chars)
# \W = all else
# \s = space, tab, newline (space chars)
# \S = all else


print('-'*100)
# define your own
# [a-z], [1-5], [a-zA-Z] = indicate specific range
# [aeiou] = indicate specific chars
# [*/{}] NOTE: inside of square brackets special characters are not treated as such
# [^] NOTE: caret is used to indicate negation - so all the chars inside the brackets will NOT be matched.
# NOTE: this is only INSIDE []. In normal regex, caret indicates start of expression
r = re.compile(r'^Hello')
mo = r.search('Hello world')
print(mo.group())
mo = r.search('z Hello world')
# print(mo.group())  # produces an error

# $ = match the end
r = re.compile(r'Hello$')
mo = r.search('world Hello')
print(mo.group())
# ^...$ = the entire string needs to match
r = re.compile(r'^Hello$')
mo = r.search('Hello')  # this is the only one that matches!
print(mo.group())


print('-'*100)
# dot character = wildcard = will match anything
r = re.compile('.at')
mo = r.findall('rat cat bat sat benzat')
# can combine with whole world search
print(mo)
r = re.compile(r'^H..lo$')
mo = r.search('Hello')  # this is the only one that matches!
print(mo.group())


print('-'*100)
# we can use .* to indicate "any number of any characters"
# NOTE: here it actually returns the stuff inside of (.*), even though "first" and "last" also need to match
r = re.compile('first: (.*)last: (.*)')
mo = r.findall('first: ilja, last: moi')
print(mo)
# .*? is an extention that will look for shortest, not most greedy option
r = re.compile('<.*>')  # greedy
mo = r.findall('<first part> second part>')
print(mo)
r = re.compile('<.*?>')  # not
mo = r.findall('<first part> second part>')
print(mo)
# NOTE: the only thing that .* does not match are new lines = \n. Unless you pass the following argument: re.compile('.*', re.DOTALL)


print('-'*100)
# to make case insensitive pass re.I as an argument -
r = re.compile(r'robocop', re.I)
mo = r.search('ROBOCOP LOUD!!!')
print(mo.group())


print('-'*100)
# we can use substitutions. The first passed argument = new phrase to be subed, the second passed argument = old phrase where to sub
# NOTE: we're saying find "Agent " with a space at the end. Then find all "word" characters until the next space. Replace the two together.
r = re.compile(r'Agent (\w)+')
print(r.sub('CENSORED', 'Agent Alice gave the secret document to Agent Bob.'))

# sometimes we have to use the detected text as part of the substitution. we can use \1 \2 \3 to indicate the group from which that text is to be taken
r = re.compile(r'Agent (\w)\w*')
print(r.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))


print('-'*100)
# for complicated regexes we can enter the VERBOSE mode and write them with comments, spaces, and newlines
# NOTE the triple quotes
r = re.compile(r"""(
    (\d\d\d) # first
    . # second
    (\d\d\d\d) # third
)""", re.VERBOSE)

# r = re.compile(r'(\d\d\d).(\d\d\d\d)')
mo = r.search('phone is 123-4567')
print(mo.groups())

# NOTE if you wanted to combine more than one argument to re.compile you'd have to use a pipe
r = re.compile('a', re.VERBOSE | re.DOTALL | re.IGNORECASE)

# confusion with ?
# i can either mean non greedy search
# or if placed at the end of ()? it means 0 or 1 occurences

numRegex = re.compile(r'\d+')
print(numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens'))

# . = any char
# .* = any number of any chars
# .*? = any number of any chars, but nongreedy - remember: <serve human> for dinner>
