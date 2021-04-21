

import smtplib

from email.mime.text import MIMEText

msg = MIMEText("This is a test mail ... ")

msg['Subject'] = 'TEST MAIL'
msg['From'] = "AMT@Gmail.com"
msg['To'] = ["email.com", "email.com"]

s = smtplib.SMTP('smtp.gmail.com')
s = smtplib.SMTP_SSL_PORT
s.login("amtkmr.1990.ap", "INDEPENDENCE")
s.send_message(msg)
s.quit()

import smtplib

server = smtplib.SMTP ( 'smtp.gmail.com', 587 )
server.starttls ()
server.login ( "email.com", "INDEPENDENCE" )

msg = "YOUR MESSAGE!"
server.sendmail ( "amt@gmail.com", "email.com", msg )
server.quit ()