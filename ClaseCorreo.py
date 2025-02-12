import smtplib
from email.message import EmailMessage

class MandarEmail:
    def __init__(self, username, password):
        self.smtp_server = "smtp01.educa.madrid.org"
        self.port = 587
        self.username = username
        self.password = password
        self.server = None
    
    def create_message(self, subject, body, from_email, to_email):
        message = EmailMessage()
        message.set_content(body)
        message['Subject'] = subject
        message['From'] = from_email
        message['To'] = to_email
        return message
    
    def connect(self):
        self.server = smtplib.SMTP(self.smtp_server, self.port)
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.username, self.password)
    
    def enviar(self, subject, body, from_email, to_email):
        message = self.create_message(subject, body, from_email, to_email)
        if self.server is None:
            self.connect()
        self.server.send_message(message)
    
    def disconnect(self):
        if self.server:
            self.server.quit()