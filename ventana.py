import tkinter as tk
from temas import LightTheme
from temas import DarkTheme
from conexion import Conexion
import tkinter.messagebox as MessageBox
from jugador import Jugador
import threading
from CrearGrafica import CrearGrafica



class Ventana(tk.Tk):
    def __init__(self, tema, title, width, height):
        super().__init__()

        self.nickname = ""
        self.password = ""
        self.email = ""

        self.width = width
        self.height = height
        self.miTitulo = title

        if tema:
            self.color_cabecera = LightTheme().Color_Cabecera
            self.color_fondo = LightTheme().Color_Fondo
            self.color_footer = LightTheme().Color_Pie
            self.color_texto = LightTheme().Color_Texto
        else:
            self.color_cabecera = DarkTheme().Color_Cabecera
            self.color_fondo = DarkTheme().Color_Fondo
            self.color_footer = DarkTheme().Color_Pie
            self.color_texto = DarkTheme().Color_Texto

            pantalla_ancho = self.winfo_screenwidth()
            pantalla_alto = self.winfo_screenheight()

            x = (pantalla_ancho // 2) - (self.width // 2)
            y = (pantalla_alto // 2) - (self.height // 2)

        self.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.title(self.miTitulo)
        self.resizable(False, False)

        self.conec = Conexion()
        self.conec.crearDB()
        # self.conec.cargarDatos()

        self.loginFrames()

        

    #GENERADORES DE WIDGETS
    def genTexto(self,donde,texto,size,padx,pady,pos):
       
        text= tk.Label(donde, text= texto, bg=donde.cget('bg'), font=("Constantia",size,"bold"), fg=self.color_texto )
        text.pack(anchor=pos,padx=padx, pady=pady, expand=True)
        return text
    
    def genEntry(self,donde,variable,padx,pady):
       
        entry= tk.Entry(donde, fg="#000000" , textvariable=variable)
        entry.pack(anchor="n",padx=padx, pady=pady, expand=True)
        return entry
    

    def genButton(self,donde,texto,funcion,padx,pady,pos):
       
       boton=tk.Button(donde,text=texto, command= funcion,)
       boton.pack(anchor=pos, padx=padx,pady=pady, ipadx=0, ipady=0)
       
       return boton
    
    def genLink(self,donde,texto,funcion,padx,pady,pos):
       
       boton=tk.Button(donde,text=texto, command= funcion, bg=donde.cget('bg'),fg=self.color_cabecera, relief="flat")
       boton.pack(anchor=pos, padx=padx,pady=pady)
       
       return boton
    

    #FUNCIONES DE BORRADO Y CAMBIO DE PANTALLA
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
        self.nickname=""
        self.password=""
        self.cambioPantalla()
        self.loginFrames()
        
    def ventanaRegister(self):
        self.cambioPantalla()        
        self.registerFrames()
        
    
    def VentanaPrincipal(self):
        self.cambioPantalla()
        self.mainFrames()
        

    def Logear(self, username, pwd):
        if self.conec.loginUsuario(username, pwd):
            self.nickname = username
            self.VentanaPrincipal()
        else:
            MessageBox.showwarning("Error", "El usuario o la contraseña son incorrectos. Intentalo de nuevo.")


    
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


        #BOTONES FRAMES LOGIN
        tituloCabecera=self.genTexto(self.cabecera,"Login",25,0,20,"center")

        usuarioLbl=self.genTexto(self.fondo,"Usuario", 15,0,0,"s")
        usuarioE=self.genEntry(self.fondo,self.nickname,0,0)
        passwordLbl=self.genTexto(self.fondo,"Contraseña", 15,0,0,"s")
        passwordE=self.genEntry(self.fondo,self.password,0,0)
        passwordE.configure(show="*")
        
        loginbtn=self.genButton(self.fondo,"Acceder",lambda:threading.Thread(target=self.Logear(usuarioE.get(),passwordE.get())).start(),0,20,"n")

        registerbtn=self.genLink(self.fondo,"¿No tienes cuenta? Únete",lambda:self.ventanaRegister(),0,10,"n")

        footerLbl=self.genTexto(self.footer,"Creado por Emilio, Kida y Álvaro (Curso 2ºDAM 24-25)", 10,0,0,"center")


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

        #BOTONES FRAMES REGISTRO
        tituloCabecera=self.genTexto(self.cabecera,"Registrar",25,0,20,"center")

        usuarioLbl=self.genTexto(self.fondo,"Usuario", 15,0,0,"s")
        usuarioE=self.genEntry(self.fondo,self.nickname,0,0)
        passwordLbl=self.genTexto(self.fondo,"Contraseña", 15,0,0,"s")
        passwordE=self.genEntry(self.fondo,self.password,0,0)
        passwordE.configure(show="*")
        emailLbl=self.genTexto(self.fondo,"E-mail", 15,0,0,"s")
        emailE=self.genEntry(self.fondo,self.email,0,0)
        
        loginbtn=self.genButton(self.fondo,"Registrar",lambda: threading.Thread(target=self.conec.addUsuario, args=(usuarioE.get(), emailE.get(), passwordE.get())).start(), 0, 20, "n")

        registerbtn=self.genLink(self.fondo,"Ingresar",lambda:self.ventanaLogin(),0,10,"n")




        footerLbl=self.genTexto(self.footer,"Creado por Emilio, Kida y Álvaro (Curso 2ºDAM 24-25)", 10,0,0,"center")




    def mostrarGrafica(self):
        # Crear instancia de CrearGrafica pasando nombre de usuario
        grafica = CrearGrafica(self.nickname)
        # Llamar metodo para dibujar grafica
        grafica.dibujar_grafica(self.fondo)
        


    def mainFrames(self):
        self.geometry("800x500")
        self.title("Juego KEA")

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

        #BOTONES MAIN FRAME
        lblTitulo=self.genTexto(self.cabecera,f"Bienvenido {self.nickname}",30,0,0,"n")
        btnMainMandarCorreo=self.genButton(self.sidebar,"Mandar al correo",{},5,10,"center")
        
        btnMainMostrarGrafica = self.genButton(self.sidebar,"Mostrar gráfica",lambda: self.mostrarGrafica(),5, 10, "center")
        
        btnMainGenerarPDF=self.genButton(self.sidebar,"Generar PDF",{},5,10,"center")
        btnMainCerrarSesion=self.genButton(self.sidebar,"Cerrar sesión",lambda:self.ventanaLogin(),5,20,"s")
