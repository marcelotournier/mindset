from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys


recipients = [str(sys.argv[1])] 
emaillist = [elem.strip().split(',') for elem in recipients]
msg = MIMEMultipart()
msg['Subject'] = "Seu Perfil Mindset"
msg['From'] = 'relatoriodisc@gmail.com'
msg['Reply-to'] = 'relatoriodisc@gmail.com'
 
msg.preamble = 'Multipart massage.\n'
 
part = MIMEText("Oi!  Em anexo, segue o seu Perfil Mindset.  Abs!")
msg.attach(part)
 
part = MIMEApplication(open(str(sys.argv[2]),"rb").read())
part.add_header('Content-Disposition', 'attachment', filename=str(sys.argv[2]))
msg.attach(part)
 

server = smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.login("relatoriodisc@gmail.com", "PASSWORD_CHANGE_IT_NOW")
 
server.sendmail(msg['From'], emaillist , msg.as_string())
