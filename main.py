from ventana import Ventana

root = Ventana(True,400, 500, "SGE- 2DAM - AF EG KG", 500, 20)

root.loginFrames("Login")
root.resizable(False,False)

tituloCabecera=root.genTexto(root.cabecera,"Login",25,0,20,"center")


usuarioLbl=root.genTexto(root.fondo,"Usuario", 15,0,0,"s")
usuarioE=root.genEntry(root.fondo,0,0)
passwordLbl=root.genTexto(root.fondo,"Contraseña", 15,0,0,"s")
passwordE=root.genEntry(root.fondo,0,0)

Loginbtn=root.genButton(root.fondo,"Acceder",{},0,20,"n")

Loginbtn=root.genLink(root.fondo,"¿No tienes cuenta? Únete",lambda:root.RegisterWin,0,10,"n")




footerLbl=root.genTexto(root.footer,"Creado por Emilio, Kida y Álvaro (Curso 2ºDAM 24-25)", 10,0,0,"center")


root.mainloop()