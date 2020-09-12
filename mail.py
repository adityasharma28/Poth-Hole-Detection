#!/usr/bin/python36

import os
import smtplib
import getpass
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

username= "rawatchetan133@gmail.com"

google_mail = smtplib.SMTP(host='smtp.gmail.com', port=587)

google_mail.starttls()
print("enter your password ")
password=getpass.getpass()
google_mail.login(username , password)
msg=MIMEMultipart()
text = MIMEText("This is a mail")
msg.attach(text)
fp = open('C:\Users\Asus\Desktop\pothole_detection_v02\graypothholeresultnew.jpg','rb')
image= MIMEImage(fp.read())
fp.close()
msg.attach(image)

google_mail.sendmail(username , 'chetanrawat@live.com' , msg.as_string())
print("successful")
google_mail.quit()
