import mysql.connector
import bcrypt
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox

class Conexion():
    def __init__(self):
        self.user = "root"
        self.pwd = "123456"
        self.host = "localhost"
        self.bd = "juegokea"
        self.conn = None
        
        self.root = tk.Tk()
        self.root.withdraw()

    def conectar(self):
        try:
            self.conn = mysql.connector.connect(user=self.user, password=self.pwd, host=self.host, database=self.bd, port="3307")
            if self.conn.is_connected():
                return True
        except Error as e:
            print(f"Error de conexión: {e}")
        return False

    def cerrar_conexion(self):
        if self.conn.is_connected():
            self.conn.close()

    def crearDB(self):
        if self.conectar():
            try:
                cursor = self.conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS jugadores (
                        username VARCHAR(30) PRIMARY KEY,
                        email VARCHAR(100) NOT NULL UNIQUE,
                        password VARCHAR(255) NOT NULL
                    );
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS partidas (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        fecha DATETIME NOT NULL,
                        duracion INT NOT NULL
                    );
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS puntuaciones (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        jugador_username VARCHAR(30),
                        partida_id INT,
                        puntos INT NOT NULL,
                        FOREIGN KEY (jugador_username) REFERENCES jugadores(username) ON DELETE CASCADE,
                        FOREIGN KEY (partida_id) REFERENCES partidas(id) ON DELETE CASCADE,
                        UNIQUE (jugador_username, partida_id)
                    );
                """)
                self.conn.commit()
            except Error as e:
                print(f"Error creando la bbdd: {e}")
            finally:
                cursor.close()
                self.cerrar_conexion()

    def cargarDatos(self):
        if self.conectar():
            try:
                cursor = self.conn.cursor()

                password_juan = bcrypt.hashpw('password123'.encode(), bcrypt.gensalt()).decode()
                password_maria = bcrypt.hashpw('password456'.encode(), bcrypt.gensalt()).decode()
                password_pedro = bcrypt.hashpw('password789'.encode(), bcrypt.gensalt()).decode()
                password_ana = bcrypt.hashpw('password987'.encode(), bcrypt.gensalt()).decode()

                cursor.execute("""
                    INSERT INTO jugadores (username, email, password) VALUES
                    ('juan123', 'juan@example.com', '{}'),
                    ('maria456', 'maria@example.com', '{}'),
                    ('pedro789', 'pedro@example.com', '{}'),
                    ('ana987', 'ana@example.com', '{}');
                """.format(password_juan, password_maria, password_pedro, password_ana))

                cursor.execute("""
                    INSERT INTO partidas (fecha, duracion) VALUES
                    ('2025-02-06 10:00:00', 30),
                    ('2025-02-06 11:00:00', 45),
                    ('2025-02-06 12:00:00', 60),
                    ('2025-02-06 13:00:00', 20);
                """)

                cursor.execute("""
                    INSERT INTO puntuaciones (jugador_username, partida_id, puntos) VALUES
                    ('juan123', 1, 15), ('maria456', 1, 20), ('pedro789', 2, 30), 
                    ('ana987', 2, 25), ('juan123', 3, 40), ('maria456', 3, 35),
                    ('pedro789', 4, 10), ('ana987', 4, 18);
                """)
                self.conn.commit()
            except Error as e:
                print(f"Error cargando datos: {e}")
            finally:
                cursor.close()
                self.cerrar_conexion()

    def execQuery(self, query):
        if self.conectar():
            try:
                cursor = self.conn.cursor()
                cursor.execute("USE juegokea")
                cursor.execute(query)
                results = cursor.fetchall()
                self.conn.commit()
                return results
            except Error as e:
                print(f"Error en la consulta: {e}")
            finally:
                cursor.close()
                self.cerrar_conexion()

    def existeUsuario(self, username):
        query = f'SELECT * FROM jugadores WHERE username="{username}";'
        return bool(self.execQuery(query))

    def loginUsuario(self, username, password):
        exito = False
        if self.existeUsuario(username):
            # Buscar el hash de la pass almacenada
            query = f'SELECT password FROM jugadores WHERE username="{username}";'
            usuario = self.execQuery(query)
            if usuario:
                # El primer valor de usuario es el hash almacenado en la base de datos
                stored_hash = usuario[0][0]
                # Verificar si la contraseña proporcionada coincide con el hash almacenado
                if bcrypt.checkpw(password.encode(), stored_hash.encode()):
                    exito = True
        return exito

    def addUsuario(self, username, email, password):
        exito = False
        if not self.existeUsuario(username):
            # Generar el "salt" y hash de la pass antes de almacenarla
            hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            query = f'INSERT INTO jugadores (username, email, password) VALUES ("{username}", "{email}", "{hashed_pw.decode()}");'
            self.execQuery(query)
            exito = True
            # Mostrar el mensaje de exito usando messagebox
            messagebox.showinfo("Registro exitoso", f"¡Usuario '{username}' registrado correctamente!")
        else:
            # Mostrar el mensaje si el usuario ya existe
            messagebox.showwarning("Error", f"El usuario '{username}' ya existe.")
        return exito
