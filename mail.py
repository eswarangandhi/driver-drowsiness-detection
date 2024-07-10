## import packages

import os
import time                                     
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
import imghdr
from datetime import datetime 

## define function
def report_send_mail(image_path):
    '''
    This function sends mail
    '''
    now=datetime.now()
    current_time=now.strftime("%H:%M:%S")
    label = "Hello! User\
    Alert message from DROWSY DRIVING ALERT\
    driver is feeling drowsy on "+ current_time

    with open(image_path, 'rb') as f:
        img_data = f.read()
    fromaddr = "eswar20030611@gmail.com"
    toaddr = "eswar20030611@gmail.com"
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    msg['Subject'] = "Alert"
    body = label
    msg.attach(MIMEText(body, 'plain'))  # attach plain text
    image = MIMEImage(img_data, name=os.path.basename(image_path))
    msg.attach(image) # attach image
    s = smtplib.SMTP('smtp.gmail.com',587) 
    s.starttls() 
    s.login(fromaddr, "dsdxabafxligollz")
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit()

report_send_mail('image.jpg')
