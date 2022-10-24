from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'shahzeb.nasir.memon@gmail.com'
email_password = 'ggegffkigjknhjzk'

email_receiver = 'sabas13647@cadolls.com'  #Generate the email from temp-mail

subject = 'Hello From Python!'
body = """
If you are receiving this email, It means that I was able to send you an email from Pycharm using Python!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
