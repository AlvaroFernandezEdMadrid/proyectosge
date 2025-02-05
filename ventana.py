import tkinter as tk
from temas import LightTheme
from temas import DarkTheme



class Ventana(tk.Tk):
    def __init__(self,tema, ancho, alto, titulo, posx, posy):
        

        #self. scPos= win.winfo_rooty() - win.winfo_x()
        
        
        self.titulo=titulo
        self.ancho=ancho
        self.alto=alto
        self.posx=posx
        self.posy=posy

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

        

        
        super().__init__()
        self.title(titulo)
        self.geometry(f"{self.ancho}x{self.alto}+{self.posx}+{self.posy}")
        



    def loginFrames(self,titulo):
        self.cabecera= tk.Frame(
            self,
            bg = self.color_cabecera,
            height = 80,
            highlightbackground="black",
            highlightthickness=1
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
    
    def RegisterWin(self,donde,titulo):
        registerWin=tk.Toplevel(donde,titulo)

        self.cabecera= tk.Frame(
            self,
            bg = self.color_cabecera,
            height = 80,
            highlightbackground="black",
            highlightthickness=1
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
        



        
    def genTexto(self,donde,texto,size,padx,pady,pos):
       
        text= tk.Label(donde, text= texto, bg=donde.cget('bg'), font=("Constantia",size,"bold"), fg=self.color_texto , wraplength= self.ancho)
        text.pack(anchor=pos,padx=padx, pady=pady, expand=True)
        return text
    
    def genEntry(self,donde,padx,pady):
       
        entry= tk.Entry(donde, fg="#000000")
        entry.pack(anchor="n",padx=padx, pady=pady, expand=True)
        return entry
    

    def genButton(self,donde,texto,funcion,padx,pady,pos):
       
       boton=tk.Button(donde,text=texto, command= funcion)
       boton.pack(anchor=pos, padx=padx,pady=pady, ipadx=10, ipady=10 )
       
       return boton
    
    def genLink(self,donde,texto,funcion,padx,pady,pos):
       
       boton=tk.Button(donde,text=texto, command= funcion, bg=donde.cget('bg'),fg=self.color_cabecera, relief="flat")
       boton.pack(anchor=pos, padx=padx,pady=pady)
       
       return boton

    def genSpacer(self,donde,x,y):
       spacer=tk.Label(donde,padx=x,pady=y)
       return spacer
    
