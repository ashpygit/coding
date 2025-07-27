import os
from email.message import EmailMessage
import ssl
import smtplib

email_sender='itsashishmahajan@gmail.com'
email_receiver='itzashishmahajan@gmail.com'
email_password=os.environ['snd_email']
email_subject='Test Email Subject'
email_body='''
Hello Everybody, Good Morning!
'''
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = email_subject
em.set_content(email_body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
                      smtp.login(email_sender,email_receiver)
                      smtp.sendmail(email_sender,email_receiver,em)

                      