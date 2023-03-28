from email.message import EmailMessage
## password will not be releaved due to security reason but authentication code from google.
from app2 import my_password
import ssl
import smtplib

email_sender = 'mobalouch177@gmail.com'
email_password = my_password()

#temp reciver was retrieved from tempmail.com
email_reciever = "najaleg.sivijat@rungel.net"
subject = "Don't forget to subscribe"
body = """
Please follow my GitHub account
"""

em = EmailMessage()
em['From']  = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp@gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())

