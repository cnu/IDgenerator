from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys


recipients = ['makernaren@gmail.com']
emaillist = [elem.strip().split(',') for elem in recipients]
msg = MIMEMultipart()
msg['Subject'] = "test"
msg['From'] = 'narenravi92@gmail.com'
msg['Reply-to'] = 'abcxyz@gmail.com'
 
msg.preamble = 'Multipart massage.\n'
 
part = MIMEText("Hi, please find the attached file")
msg.attach(part)
 
part = MIMEApplication(open(str('16CC0001.pdf'),"rb").read())
part.add_header('Content-Disposition', 'attachment', filename=str('16CC0001.pdf'))
msg.attach(part)
 

server = smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.login("narenravi92@gmail.com", "mad^@#$*1192!")
 
server.sendmail(msg['From'], emaillist , msg.as_string())
