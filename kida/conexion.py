import mysql.connector
import threading

class Conexion():
    def __init__(self):
        #Nickname del usuario
        self.user="root"
        #Password del usuario
        self.pwd="123456"
        #Host
        self.hostt="localhost"
        #BD 
        self.bd="juegokea"

    def conectar(self):
        self.conn= mysql.connector.connect(user=self.user, password= self.pwd, host= self.hostt, database= self.bd, port="3307" )
        return self.conn.is_connected()
    
    def crearDB(self):
           if self.conectar():
            cursor= self.conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS jugadores (username VARCHAR(30) PRIMARY KEY, email VARCHAR(100) NOT NULL UNIQUE, password VARCHAR(50) NOT NULL); ")
            cursor.execute("CREATE TABLE IF NOT EXISTS partidas (id INT AUTO_INCREMENT PRIMARY KEY, fecha DATETIME NOT NULL, duracion INT NOT NULL);")
            cursor.execute("CREATE TABLE IF NOT EXISTS puntuaciones (id INT AUTO_INCREMENT PRIMARY KEY, jugador_username VARCHAR(30), partida_id INT, puntos INT NOT NULL, FOREIGN KEY (jugador_username) REFERENCES jugadores(username) ON DELETE CASCADE, FOREIGN KEY (partida_id) REFERENCES partidas(id) ON DELETE CASCADE, UNIQUE (jugador_username,partida_id));")


    def cargarDatos(self):
         if self.conectar():
            cursor= self.conn.cursor()
            cursor.execute("INSERT INTO jugadores (username, email, password) VALUES ('juan123', 'juan@example.com', 'password123'), ('maria456', 'maria@example.com', 'password456'), ('pedro789', 'pedro@example.com', 'password789'),('ana987', 'ana@example.com', 'password987');")
            cursor.execute("INSERT INTO partidas (fecha, duracion) VALUES ('2025-02-06 10:00:00', 30), ('2025-02-06 11:00:00', 45), ('2025-02-06 12:00:00', 60), ('2025-02-06 13:00:00', 20);")
            cursor.execute("INSERT INTO puntuaciones (jugador_username, partida_id, puntos) VALUES ('juan123', 1, 15), ('maria456', 1, 20), ('pedro789', 2, 30), ('ana987', 2, 25), ('juan123', 3, 40),('maria456', 3, 35), ('pedro789', 4, 10),('ana987', 4, 18);")
            self.conn.commit()
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
        if self.execQuery(f'SELECT * FROM jugadores WHERE username="{username}";'):
            existe=True
            print(username)
        return existe
    
    def loginUsuario(self,usernam,pwd):
        exito=False
        if(self.existeUsuario(usernam)):
            self.usuario=self.execQuery(f'SELECT * FROM jugadores WHERE username="{usernam}" AND password="{pwd}";')            
            exito=True
        return exito


    def addUsuario(self,username,email,pwd):
        exito=False
        
        if(not self.existeUsuario(username)):
            self.execQuery(f'INSERT INTO jugadores (username,email,password) VALUES ("{username}","{email}","{pwd}");')
            exito=True 
        
        return exito

    