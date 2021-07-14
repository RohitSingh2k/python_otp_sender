# Prerequisits : -
#       1) pip install python-decouple
#       2) create .env file into the directory where your main file exist
#       3) Add these two lines into .env file: -
#
#                   EMAIL_ADDERSS="your email address"
#                   PASSWORD="your email password"
#
#       4) add index.html and edit it as you like it just replace otp section with {% OTP %}

"""
    Author  : Rohit Singh
    Purpose : Made OTP sending easy.
"""

from email.message import EmailMessage
from decouple import config
import smtplib, ssl, random

# read html file
data = """ """
with open("./python_otp/index.html") as file:
    data = file.read()
   
    
def otp_for(reciever_email):
    email = config('EMAIL_ADDRESS')
    email_password = config('PASSWORD')

    msg = EmailMessage()
    msg['Subject'] = 'OTP test'
    msg['From'] = email
    msg['To'] = reciever_email

    # generate otp
    otp = str(random.randint(1000,9999))
    
    # adding otp to html
    page = data.replace('{% OTP %}',otp)

    msg.add_alternative(page, subtype='html')
    
    # creating secure ssl
    context = ssl.create_default_context()
    
    # creating server
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login(email, email_password)
    smtp.send_message(msg)
    smtp.quit()
    
    return otp

