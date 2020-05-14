import re
# stron pw is one that
# has 8 chars
# has upper and lowercase letters
# has at least one digit

L = ['a', 'b', 'c', 'd', 'r', 'v']

r_eight = re.compile(r'.{8}')
r_num = re.compile(r'[0-9]')
r_upper = re.compile(r'[A-Z]')
r_lower = re.compile(r'[a-z]')
for l in L:
    mo_eight = r_eight.search(l)
    mo_num = r_num.search(l)
    mo_upper = r_upper.search(l)
    mo_lower = r_lower.search(l)
    try:
        mo_eight.group()
        mo_num.group()
        mo_upper.group()
        mo_lower.group()
    except:
        print('shitty pw')
    else:
        print(f'this password works: {l}')
