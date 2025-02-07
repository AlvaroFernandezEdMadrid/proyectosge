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
    

    def execQuery(self,query):
        if self.conectar():
            cursor= self.conn.cursor()
            cursor.execute("USE juegokea")
            cursor.execute(query)
            results=cursor.fetchall()
            self.conn.commit()
            cursor.close()
            self.conn.close()
            return results

    def existeUsuario(self,username):
        existe=False
        if self.execQuery(f'SELECT j FROM Jugador j WHERE j.username LIKE {username}'):
            existe=True
        return existe
    
    def loginUsuario(self,jugador):
        exito=False
        self.execQuery("CREATE TABLE IF NOT EXISTS Jugadores (nickname Varchar(30),email Varchar(70) password Varchar(30))")

        if(self.existeUsuario(jugador.nickname)):
            self.execQuery(f'SELECT j FROM Jugador j WHERE j.username LIKE {jugador.username} AND j.password LIKE {jugador.password}')
            exito=True
        return exito


    def addUsuario(self,jugador):
        exito=False
        
        if(not self.existeUsuario(jugador.username)):
            self.execQuery(f'INSERT INTO Jugador (username,email,pwd) VALUES ({jugador.username},{jugador.email},{jugador.pwd});')
            exito=True 
        
        return exito

    