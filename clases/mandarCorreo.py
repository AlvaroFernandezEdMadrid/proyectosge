import tkinter as tk
from kida.correoBien import MandarEmail
from CrearGrafica import CrearGrafica

def enviar_email():
    username = entry_username.get()
    password = entry_password.get()
    from_email = f"{username}@educa.madrid.org"
    to_email = entry_to_email.get()
    subject = entry_subject.get()
    body = entry_body.get()

    email_sender = MandarEmail(username, password)
    email_sender.enviar(subject, body, from_email, to_email)
    email_sender.disconnect()

root = tk.Tk()
root.title("Formulario Correo")

tk.Label(root, text="Usuario:").grid(row=0, column=0, padx=10, pady=5)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Contrasena:").grid(row=1, column=0, padx=10, pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Correo destinatario:").grid(row=2, column=0, padx=10, pady=5)
entry_to_email = tk.Entry(root)
entry_to_email.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Asunto:").grid(row=3, column=0, padx=10, pady=5)
entry_subject = tk.Entry(root)
entry_subject.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Cuerpo del correo:").grid(row=4, column=0, padx=10, pady=5)
entry_body = tk.Entry(root)
entry_body.grid(row=4, column=1, padx=10, pady=5)

btn_enviar = tk.Button(root, text="Enviar Correo", command=enviar_email)
btn_enviar.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()