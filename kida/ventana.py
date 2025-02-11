import tkinter as tk
from temas import LightTheme
from temas import DarkTheme
from conexion import Conexion
from jugador import Jugador
import threading
from correoBien import MandarEmail
from ClasePdf import Pdf



class Ventana(tk.Tk):
    def __init__(self,tema,title,weight, height, x, y):
        super().__init__()

        self.nickname=""
        self.password=""
        self.email=""
        
        self.weight = weight
        self.height = height
        self.x = x
        self.y = y
        self.miTitulo = title
        if(tema==True):
            self.color_cabecera=LightTheme().Color_Cabecera
            self.color_fondo=LightTheme().Color_Fondo
            self.color_footer= LightTheme().Color_Pie
            self.color_texto=LightTheme().Color_Texto
        else:
            self.color_cabecera=DarkTheme().Color_Cabecera
            self.color_fondo=DarkTheme().Color_Fondo
            self.color_footer= DarkTheme().Color_Pie
            self.color_texto=DarkTheme().Color_Texto
        
        self.geometry("%dx%d+%d+%d" %(self.weight, self.height, self.x, self.y))
        self.title(self.miTitulo)
        self.resizable(False, False)

        self.conec=Conexion()
        self.conec.crearDB()
        #self.conec.cargarDatos()

        #parametro correo
        self.correo = MandarEmail("emilio.garcia15", "$iz5QOa=FJ")

        
        self.loginFrames()
        

    #WIDGETS
    def genTexto(self,donde,texto,size,padx,pady,pos):
       
        text= tk.Label(donde, text= texto, bg=donde.cget('bg'), font=("Constantia",size,"bold"), fg=self.color_texto )
        text.pack(anchor=pos,padx=padx, pady=pady, expand=True)
        return text
    
    def genEntry(self,donde,variable,padx,pady):
       
        entry= tk.Entry(donde, fg="#000000" , textvariable=variable)
        entry.pack(anchor="n",padx=padx, pady=pady, expand=True)
        return entry
    

    def genButton(self,donde,texto,funcion,padx,pady,pos):
       
       boton=tk.Button(donde,text=texto, command= funcion)
       boton.pack(anchor=pos, padx=padx,pady=pady, ipadx=0, ipady=0 )
       
       return boton
    
    def genLink(self,donde,texto,funcion,padx,pady,pos):
       
       boton=tk.Button(donde,text=texto, command= funcion, bg=donde.cget('bg'),fg=self.color_cabecera, relief="flat")
       boton.pack(anchor=pos, padx=padx,pady=pady)
       
       return boton
    


    def deleteInFrames(self,donde):
        for widget in donde.winfo_children():
            widget.destroy()

    def cambioPantalla(self):
        self.fondo.destroy()
        if "sidebar" in dir(self):
            self.sidebar.destroy()
        self.cabecera.destroy()
        self.footer.destroy()

    def ventanaLogin(self):
        self.cambioPantalla()
        self.loginFrames()
        
    def ventanaRegister(self):
        self.cambioPantalla()        
        self.registerFrames()
        
    
    def VentanaPrincipal(self):
        self.cambioPantalla()
        self.mainFrames()
        

    #función para enviar el correo
    def enviarCorreo(self, username):
        self.correo.enviar("Resumen partidas", "prueba", self.correo.username, self.conec.execQuery(f'SELECT email FROM jugadores WHERE username="{username}";'))
        self.correo.disconnect()

    def generarPDF(self, username):
        pdf_creator = Pdf(
            '/media/usertar/Disco local/2DAM/SGE/2evaluacion/trabajoProgramaJugadores/templates/templatePdf.html',
            '/media/usertar/Disco local/2DAM/SGE/2evaluacion/trabajoProgramaJugadores/templates/cssCorreo.css',
        )
        puntuacion = self.conec.execQuery(f'SELECT SUM(puntos) FROM puntuaciones WHERE jugador_username="{username}";')[0][0]
        top10 = self.conec.execQuery('SELECT jugador_username, SUM(puntos) as total_puntos FROM puntuaciones GROUP BY jugador_username ORDER BY total_puntos DESC LIMIT 10;')
        context = {
            'username': username,
            'puntuacion': puntuacion,
            'top10': [{'jugador': jugador[0], 'puntuaciontotal': jugador[1]} for jugador in top10]
        }
        pdf_creator.render_pdf(f'/media/usertar/Disco local/2DAM/SGE/2evaluacion/trabajoProgramaJugadores{username}_ranking.pdf', context)

    
    #PANTALLAS


    def loginFrames(self):

        self.geometry("400x500")
        self.cabecera= tk.Frame(
            self,
            bg = self.color_cabecera,
            height = 80,
  
        )
        self.cabecera.pack(side = tk.TOP, fill = "both")
        self.cabecera.propagate(False)


        self.footer = tk.Frame(
            self,
            bg = self.color_footer,
            height = 80,
        )
        self.footer.pack(side = tk.BOTTOM, fill = "both")
        self.footer.propagate(False)


        self.fondo = tk.Frame(
            self,
            bg = self.color_fondo,
        )
        self.fondo.pack(expand = True, fill = "both")
        self.fondo.propagate(False)

        tituloCabecera=self.genTexto(self.cabecera,"Login",25,0,20,"center")

        usuarioLbl=self.genTexto(self.fondo,"Usuario", 15,0,0,"s")
        usuarioE=self.genEntry(self.fondo,self.nickname,0,0)
        passwordLbl=self.genTexto(self.fondo,"Contraseña", 15,0,0,"s")
        passwordE=self.genEntry(self.fondo,self.password,0,0)
        passwordE.configure(show="*")
        
        loginbtn=self.genButton(self.fondo,"Acceder",lambda:self.Logear(usuarioE.get(),passwordE.get()),0,20,"n")

        registerbtn=self.genLink(self.fondo,"¿No tienes cuenta? Únete",lambda:self.ventanaRegister(),0,10,"n")




        footerLbl=self.genTexto(self.footer,"Creado por Emilio, Kida y Álvaro (Curso 2ºDAM 24-25)", 10,0,0,"center")

    def Logear(self,username,pwd):
        if self.conec.loginUsuario(username,pwd):
            self.VentanaPrincipal()

    def registerFrames(self):

        self.geometry("400x500")
        self.cabecera= tk.Frame(
            self,
            bg = self.color_cabecera,
            height = 80,
  
        )
        self.cabecera.pack(side = tk.TOP, fill = "both")
        self.cabecera.propagate(False)


        self.footer = tk.Frame(
            self,
            bg = self.color_footer,
            height = 80,
        )
        self.footer.pack(side = tk.BOTTOM, fill = "both")
        self.footer.propagate(False)


        self.fondo = tk.Frame(
            self,
            bg = self.color_fondo,
        )
        self.fondo.pack(expand = True, fill = "both")
        self.fondo.propagate(False)

        tituloCabecera=self.genTexto(self.cabecera,"Registrar",25,0,20,"center")

        usuarioLbl=self.genTexto(self.fondo,"Usuario", 15,0,0,"s")
        usuarioE=self.genEntry(self.fondo,self.nickname,0,0)
        passwordLbl=self.genTexto(self.fondo,"Contraseña", 15,0,0,"s")
        passwordE=self.genEntry(self.fondo,self.password,0,0)
        passwordE.configure(show="*")
        emailLbl=self.genTexto(self.fondo,"E-mail", 15,0,0,"s")
        emailE=self.genEntry(self.fondo,self.email,0,0)
        
        loginbtn=self.genButton(self.fondo,"Registrar",lambda:self.conec.addUsuario(usuarioE.get(),emailE.get(),passwordE.get()),0,20,"n")

        registerbtn=self.genLink(self.fondo,"Ingresar",lambda:self.ventanaLogin(),0,10,"n")




        footerLbl=self.genTexto(self.footer,"Creado por Emilio, Kida y Álvaro (Curso 2ºDAM 24-25)", 10,0,0,"center")




    def mainFrames(self):
        self.geometry("800x500")
        self.title("Juego KAE")

        self.cabecera= tk.Frame(
            self,
            bg = self.color_cabecera,
            height = 80,
  
        )
        self.cabecera.pack(side = tk.TOP, fill = "both")
        self.cabecera.propagate(False)

        self.sidebar = tk.Frame(
            self,
            bg = self.color_cabecera,
            width= 200,
        )
        self.sidebar.pack(side = tk.LEFT, fill = "both")
        self.sidebar.propagate(True)

        

        self.fondo = tk.Frame(
            self,
            bg = self.color_fondo,
        )
        self.fondo.pack(expand = True, fill = "both")
        self.fondo.propagate(False)

        lblTitulo=self.genTexto(self.cabecera,"Juego KEA",30,0,0,"n")
        btnMainMandarCorreo=self.genButton(self.sidebar,"Mandar al correo",lambda:threading.Thread(target=self.enviarCorreo, args=(self.nickname,)).start(),5,10,"center")
        btnMainMostrarGrafica=self.genButton(self.sidebar,"Mostrar gráfica",{},5,10,"center")
        btnMainGenerarPDF=self.genButton(self.sidebar,"Generar PDF",lambda:threading.Thread(target=self.generarPDF, args=(self.nickname,)).start(),5,10,"center")
        btnMainCerrarSesion=self.genButton(self.sidebar,"Cerrar sesión",lambda:self.ventanaLogin(),5,20,"s")
