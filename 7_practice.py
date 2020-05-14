import re
# 1.  What is the function that creates Regex objects?
# r = re.compile()
# mo = r.search()
# print(mo.group())

# 2. Why are raw strings often used when creating Regex objects?
# we use real strings so that python treats backslash as a real character and so we don't have to write \\ all the time

# 3. What does the search() method return?
# a match object, which we can then "unpack" using .group()

# 4. How do you get the actual strings that match the pattern from a Match object?
# .group(x) or .groups()

# 5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?
# 0 = entire expression, 1 = (ddd), 2 = (ddd-dddd)

# 6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?
# escape them with \

# 7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?
# whether groups were specified or not

# 8. What does the | character signify in regular expressions?
# pipe = either or

# 9. What two things does the ? character signify in regular expressions?
# 1) find 0-1 occurences, 2))run non-greedy

# 10. What is the difference between the + and * characters in regular expressions?
# + = find 1 or more, * = find 0 or more

# 11. What is the difference between {3} and {3,5} in regular expressions?
# exactly 3 vs 3-5

# 12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?
# digits, words, spsaces

# 13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?
# reverse of above

# 14. What is the difference between .* and .*??
# ,* = any number of any characteers, .*? = find the shortest least greedy expression

# 15. What is the character class syntax to match all numbers and lowercase letters?
# [0-9a-z]

# 16. How do you make a regular expression case-insensitive?
# , re.I]

# 17. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?
# all chars except \n, all chars

# 18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?
# X drummers, X pipers, etc

# 19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?
# triple comments and shit

# 20. How would you write a regex that matches a number with commas for every three digits? It must match the following:
# list_of_strings = ['42', '1,234', '6,368,745', '12,34,567', '1234']
# r = re.compile(r'^\d{1,3}(,\d{3})*$')
# for s in list_of_strings:
#     mo = r.search(s)
#     try:
#         print(mo.group())
#     except:
#         print('not found mate')
# learnings:
# 1 - strings need to be ONLY numbers to be able to use ^ and $. Make a list, iterate through it
# 2 - search() and findall() produce different results! use appropriately.


# 21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:
# s = """
# 'Haruto Watanabe'
# 'Alice Watanabe'
# 'RoboCop Watanabe'
# but not the following:
#
# 'haruto Watanabe' (where the first name is not capitalized)
# 'Mr. Watanabe' (where the preceding word has a nonletter character)
# 'Watanabe' (which has no first name)
# 'Haruto watanabe' (where Watanabe is not capitalized)
# """
# r = re.compile(r'([A-Z](\w)*\sWatanabe)')
# mo = r.findall(s)
# print(mo)
# print(mo.group())

# 22. How would you write a regex that matches a sentence
# where the first word is either Alice, Bob, or Carol;
# the second word is either eats, pets, or throws;
# the third word is apples, cats, or baseballs; and the sentence ends with a period?
# This regex should be case-insensitive. It must match the following:

s = """
'Alice eats apples.'
'Bob pets cats.'
'Carol throws baseballs.'
'Alice throws Apples.'
'BOB EATS CATS.'
but not the following:

'RoboCop eats apples.'
'ALICE THROWS FOOTBALLS.'
'Carol eats 7 cats.'
"""

L = s.split('\n')
L.pop(0)
L = [i.strip("\'") for i in L]
print(L)

r = re.compile(r"""(
    ^(Alice|Bob|Carol)
    \s
    (eats|pets|throws)
    \s
    (apples|cats|baseballs)
    \.
)""", re.I | re.VERBOSE)
for i in L:
    mo = r.search(i)
    try:
        print(mo.group())
    except:
        print('not found')
