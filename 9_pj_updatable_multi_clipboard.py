import pyperclip
import sys

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}


if len(sys.argv) < 2:
    print('Usage: py mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyword = sys.argv[1]

if keyword in TEXT:
    # print(TEXT[keyword])
    print('copied to clipboard!')
    pyperclip.copy(TEXT[keyword])
else:
    print('no such keyword')
    sys.exit()
