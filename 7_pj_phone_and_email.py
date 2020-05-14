import pyperclip as p
import re

# get the text off the clipboard, use pyperclip
text = p.paste()
text = """
123-456-7890
123.456.7890
132456-7890
123 123 1234
ilja.moi@gmail.com
iljazasdfasdf@gmail.comz
i234-134@gmail.com
"""

# define a list we'll populate
return_list = []


# find all phone numbers
phone_r = re.compile(r"""(
    (\d{3} | \(\d{4})? # 123 or # (123) #we're having to use parentheses here coz it might be one or the other
    (\s|-|\.)? # separator
    (\d{3}) # first 3 digits
    (\s|-|\.)? # separator
    (\d{4}) # last 4 digits
    # (\s*(ext|x|ext.)\s*\d{2,5})? # extention
)""", re.VERBOSE)
mo = phone_r.findall(text)
for i in mo:
    # print(i)
    return_list.append(i[0])


# find all emails
email_r = re.compile(r"""(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9._]+
    (\.
    [a-zA-Z]+) # not sure why you need brackets here... but I think coz .something is like one thing
)""", re.VERBOSE)
mo = email_r.findall(text)
for i in mo:
    # print(i)
    return_list.append(i[0])


# neantly format both into a single string to paste
return_str = '\n'.join(return_list)
return_str = return_str.replace(" ", "")
return_str = return_str.replace("-", "")
return_str = return_str.replace(".", "")
print(return_str)

# return to the clipboard
p.copy(return_str)
