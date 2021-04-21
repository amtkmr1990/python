import imaplib
import email

# Server: imap-mail.outlook.com
# SSL: true-implicit
# Port: 993 (default)
# User: pat@hotmail.com

i = imaplib.IMAP4_SSL('imap-mail.outlook.com',993)
i.login('email.com', 'password')
print(i.select())
t, l = i.list()
print(t)
#print(l)
#for i in l:
    #print(i)
print(i.search(None,'ALL'))
rv, msg = i.fetch('1767','(RFC822)')
print(email.message_from_bytes(msg[0][1]))
print(msg['Subject'])
i.close()
i.logout()
