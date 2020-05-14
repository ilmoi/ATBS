import pyperclip
import sys
import shelve

# uncomment and run once!
# TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
#         'busy': """Sorry, can we do this later this week or next week?""",
#         'upsell': """Would you consider making this a monthly donation?"""}
# file =shelve.open('phrase_db')
# for key, value in list(TEXT.items()):
#     file[key] = value
# # test
# print(file['agree'])
# file.close()

if len(sys.argv) < 2:
    print('Usage: python 9_pj_mcw [action - save / list / item to load]')
    sys.exit()

first = sys.argv[1]

file = shelve.open('phrase_db')

if first == 'save':
    keyword = sys.argv[2]
    text = pyperclip.paste()
    file[keyword] = text

elif first == 'delete':
    second = sys.argv[2]
    if second == 'all':
        confirm = input('are you sure you want to wipe the dic?')
        if confirm == 'yes':
            for key in file.keys():
                del file[key]
        print("done! clean like a baby's ass?[wtf]")
    else:
        second = sys.argv[2]
        if second in file.keys():
            del file[second]
            print('deleted!')
        else:
            print('no such keyword')
            sys.exit()

elif first == 'list':
    print('___current contents are:___')
    for key, value in list(file.items()):
        print(f'{key}: {value}')

else:
    if first in file.keys():
        pyperclip.copy(file[first])
        print('copied to clipboard!')
    else:
        print('no such keyword')
        sys.exit()

file.close()
