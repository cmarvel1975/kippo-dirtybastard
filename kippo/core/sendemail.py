import smtplib
from email.mime.text import MIMEText
from kippo.core.config import config    

def sendEmail(subject,  message):
    cfg = config()
    emailAlerts = cfg.getboolean('honeypot', 'email_alerts')
    if not emailAlerts:
        return
    
    msg = MIMEText(message)
    msg['Subject'] = subject
    
    toEmail = cfg.get('honeypot', 'to_email')
    msg['To'] = toEmail
    
    fromEmail = cfg.get('honeypot',  'from_email')
    msg['From'] = fromEmail
    
    smtpServer = cfg.get('honeypot',  'smtp_server')
    s = smtplib.SMTP(smtpServer)
    s.sendmail(fromEmail, [toEmail], msg.as_string())
