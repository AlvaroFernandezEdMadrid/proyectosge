import mysql.connector


class Conexion():
    def __init__(self, user,pwd):
        #Nickname del usuario
        self.user=user
        #Password del usuario
        self.pwd=pwd
        #Host
        self.hostt="localhost"
        #BD 
        self.bd="proyectoSGE"

    def conectar(self):
        self.conn= mysql.connector.connect(user=self.user, password= self.pwd, host= self.hostt, database= self.bd )
        return self.conn.is_connected()
    
    def conectarSinRegistro(self):
        self.conn= mysql.connector.connect(user=self.user, password= self.pwd, host= self.hostt, database= self.bd )
        return self.conn.is_connected()
    

    def execQuery(self,query):
        if self.conectar():
            cursor= self.conn.cursor()
            cursor.execute(query)
            results=cursor.fetchall()
            self.conn.commit()
            cursor.close()
            return results

    def existeUsuario(self,username):
        existe=False
        if self.execQuery(f"SELECT u FROM Usuario u WHERE u.username LIKE " + {username} ):
            existe=True
        return existe
    
    def loginUsuario(self,jugador):
        exito=False
        
        if(self.existeUsuario(jugador.username)):

            

        return exito