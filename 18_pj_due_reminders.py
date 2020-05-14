"""this script finds all debtors and emails them a message."""

import smtplib
import openpyxl
import os

os.chdir('/Users/ilja/Dropbox/atbs/')

wb = openpyxl.load_workbook('dues.xlsx')
s = wb.active
# print(s['A1'].value)

names = []
emails = []
for row in range(2, s.max_row+1):
    if s['C'+str(row)].value != 'paid':
        email = s['B'+str(row)].value
        emails.append(email)
        name = s['A'+str(row)].value
        names.append(name)

print(names)
print(emails)

# part 2 =======================================================================
s = smtplib.SMTP('smtp.office365.com', 587)
s.ehlo()
s.starttls()
s.login('x', 'x')

for name, email in zip(names, emails):
    body = f'Subject: Due date reminder. \n\nHey {name}! \nThis is a gentle reminder that you\'re past the due date on your payment. \nHope youre well otherwise. \nThanks.'
    status = s.sendmail('x', email, body)

    if status != {}:
        print(f'there was an error sending a message to {email} with {status} status')
s.quit()
