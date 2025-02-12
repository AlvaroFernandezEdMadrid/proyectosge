import tkinter as tk  # Asegúrate de importar tkinter
from PIL import Image, ImageTk
import mysql.connector
import matplotlib.pyplot as plt
import tkinter.messagebox as MessageBox


class CrearGrafica:
    def __init__(self, username):
        self.username = username
        self.db_connection = mysql.connector.connect(
            host="localhost",          
            user="root",               
            password="123456",      
            database="juegokea",
            port="3307"
        )
        self.db_cursor = self.db_connection.cursor()

    def obtener_ultimas_partidas(self):
        query = """
        SELECT p.fecha, po.puntos
        FROM partidas p
        JOIN puntuaciones po ON p.id = po.partida_id
        JOIN jugadores j ON po.jugador_username = j.username
        WHERE j.username = %s
        ORDER BY p.fecha DESC
        LIMIT 10
        """
        self.db_cursor.execute(query, (self.username,))
        partidas = self.db_cursor.fetchall()
        
        fechas = [partida[0] for partida in partidas]
        puntuaciones = [partida[1] for partida in partidas]
        return fechas, puntuaciones
    
    def dibujar_grafica(self, frame):
        fechas, puntuaciones = self.obtener_ultimas_partidas()
        
        # Verificar si no hay datos
        if not fechas:
            # Si no hay partidas, mostrar un mensaje de advertencia
            MessageBox.showwarning(title="Sin datos", message=f"No se encontraron partidas para el jugador {self.username}.")
            return
        
        # Si hay datos, crear la grafica
        plt.figure(figsize=(10, 6))
        plt.plot(fechas, puntuaciones, marker='o', color='b', linestyle='-', markersize=6, label="Puntuacion")
        plt.xlabel('Fecha de la Partida')
        plt.ylabel('Puntuacion')
        plt.title(f'Ultimas 10 partidas de {self.username}')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.legend()

        # Guardar grafica como imagen
        plt.savefig('grafica.png')
        plt.close()

        # Cargar imagen
        img = Image.open('grafica.png')
        
        # Obtener tamano del Frame donde se pinta la imagen
        frame_width = frame.winfo_width()
        frame_height = frame.winfo_height()
        
        # Mantener la relacion de aspecto al redimensionar
        img.thumbnail((frame_width, frame_height), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)

        # Label para mostrar la imagen
        label_img = tk.Label(frame, image=img_tk)
        label_img.img = img_tk  # Evitar recolector de basura
        label_img.pack(fill="both", expand=True)




