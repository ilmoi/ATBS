# Practice Questions
# 1. What is the protocol for sending email? For checking and receiving email?
# smtp / imap
# 2. What four smtplib functions/methods must you call to log in to an SMTP server?
s = smtplib.SMTP()
s.ehlo()
s.starttls()
s.login()
s.sendmail()
# 3. What two imapclient functions/methods must you call to log in to an IMAP server?
i = imapclient.IMAPClient()
i.login()
# 4. What kind of argument do you pass to imapObj.search()?
# e ['ALL']
# 5. What do you do if your code gets an error message that says got more than 10000 bytes?
# means you've exceeded memory allocated to python.
imaplib._MAXLINE = 10_000_000
# 6. The imapclient module handles connecting to an IMAP server and finding emails. What is one module that handles reading the emails that imapclient collects?
# pyzmail
# 7. When using the Gmail API, what are the credentials.json and token.json files?
# almost like password files! be very careful!
# 8. In the Gmail API, what’s the difference between “thread” and “message” objects?
# threat = chain of emails
# 9. Using ezgmail.search(), how can you find emails that have file attachments?
t = ezgmail.search('some crazy attachments').threads[0].messages[0]
t.downloadAllAttachments(downloadFolder='atts')
# 10. What three pieces of information do you need from Twilio before you can send text messages?
