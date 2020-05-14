import os
import subprocess
import imapclient
import pyzmail

os.chdir('/Users/ilja/Dropbox/atbs')

# ==============================================================================
# PART 1 - log in

i = imapclient.IMAPClient('outlook.office365.com', ssl=True)
i.login('x', 'x')

# ==============================================================================
# PART 2 - get email

i.select_folder('INBOX', readonly=True)
UIDs = i.search(['ALL'])
# print(UIDs)

raw_m = i.fetch(UIDs, ['BODY[]'])

# picking the right id
# for id in UIDs:
#     print('-'*100)
#     m = pyzmail.PyzMessage.factory(raw_m[id][b'BODY[]'])
#     subj = m.get_subject()
#     print(subj)

# id 358
m = pyzmail.PyzMessage.factory(raw_m[358][b'BODY[]'])

# ==============================================================================
# PART 3 - get attachment
for mailpart in m.mailparts:
    print('%sfilename=%r alt_filename=%r type=%s charset=%s desc=%s size=%d' % (
        '*'if mailpart.is_body else ' ',
        mailpart.filename,
        mailpart.sanitized_filename,
        mailpart.type,
        mailpart.charset,
        mailpart.part.get('Content-Description'),
        len(mailpart.get_payload())
    ))

    with open('akira.torrent', 'wb') as f:
        f.write(mailpart.get_payload())

    print('done writing!')

# ==============================================================================
# PART 4 - open the application

subprocess.Popen(['open', 'akira.torrent'])
