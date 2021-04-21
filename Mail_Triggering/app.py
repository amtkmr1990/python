import smtplib
from email.message import EmailMessage

email_header = EmailMessage()
email_header['Subject'] = 'Python SMPT mail '
email_header['From'] = 'email.com'
email_header['To'] = 'email.com, email.com'
email_content = """
Hi, 

This email is send via python smtp script 

Thanks 
"""
email_header.set_content(email_content)
gmail_username = 'email.com'
gmail_password = ''

mailer = smtplib.SMTP(host='smtp.gmail.com',port=587)
mailer.starttls()
mailer.login(gmail_username, gmail_password)
mailer.sendmail(email_header)
mailer.quit()

