"""logs into your exchange email account and automatically unsubs from every newsletter ther."""

import webbrowser
import re
import imapclient
import pyzmail

# ==============================================================================
# PART 1 - log in

i = imapclient.IMAPClient('outlook.office365.com', ssl=True)
i.login('x', 'x')

# ==============================================================================
# PART 2 - get links

i.select_folder('INBOX', readonly=True)
UIDs = i.search(['ALL'])
print(UIDs)

raw_m = i.fetch(UIDs, ['BODY[]'])

links = []

for id in UIDs:
    print('-'*100)

    m = pyzmail.PyzMessage.factory(raw_m[id][b'BODY[]'])

    subj = m.get_subject()
    print(subj)

    t = m.text_part
    txt = t.get_payload().decode(t.charset).lower().splitlines()

    r = re.compile(r'http.*?\s')

    for line in txt:
        if 'unsubscribe' in line:
            # print(line)
            mo = r.search(line)
            if mo:
                strmo = str(mo.group())
                if strmo.endswith(' '):
                    # print(True)
                    strmo = strmo[:-1]
                if strmo.endswith('>'):
                    # print(True)
                    strmo = strmo[:-1]
                # print(strmo)
                links.append(strmo)

print(links)

# ==============================================================================
# PART 3 - open them up!
for link in links:
    webbrowser.open(link)
