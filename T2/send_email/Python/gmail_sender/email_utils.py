import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def create_email(subject, body, from_addr, to_addr):
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    return msg

def send_email(config, email_msg):
    server = smtplib.SMTP(config['smtp_server'], config['smtp_port'])
    server.starttls()
    server.login(config['username'], config['app_password'])
    server.send_message(email_msg)
    server.quit()
