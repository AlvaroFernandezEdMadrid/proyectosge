import smtplib
from email.message import EmailMessage

class Correo(): 
    
    def __init__(self, mensajeCuerpo, receptor, subject):

        self.mensajeCuerpo = mensajeCuerpo
        self.receptor = receptor
        self.subject = subject
        self.remitente = "emilio.garcia15@educa.madrid.org"
        self.clienteSMTP = "smtp01.educa.madrid.org"
        self.password = ""
        self.mensaje = EmailMessage()
        

    def configurarCorreo(self):

        self.mensaje['subject'] = self.subject
        self.mensaje['From'] = self.remitente
        self.mensaje['To'] = self.receptor
        self.mensaje.set_content(self.mensajeCuerposa)

    def enviarCorreo(self):

        self.server = smtplib.SMTP(self.clienteSMTP, "587")
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.remitente, self.password)

        self.server.send_message(self.mensaje)
        self.server.quit()
