import os
from email.message import EmailMessage
import ssl
import smtplib
import imghdr

email_sender='itsashishmahajan@gmail.com'
email_receiver='itzashishmahajan@gmail.com'
email_password=os.environ['snd_email']
email_subject='Test email again'
email_body='''
This is the test email from python script.
Regards,
Ashish Mahajan
'''

em=EmailMessage()

em['From']=email_sender
em['To']=email_receiver
em['Subject']=email_subject
em.set_content(email_body)

with open('X:\\Photos\\Quotes\\2.jpg','rb') as file:
    file_data=file.read()
    file_type=imghdr.what(file.name)
    file_name=file.name
em.add_attachment(file_data, filename=file_name, subtype=file_type, maintype='image')

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())