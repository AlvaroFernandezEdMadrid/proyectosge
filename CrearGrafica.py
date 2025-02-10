import mysql.connector
import matplotlib.pyplot as plt

class CrearGrafica:
    def __init__(self, username):
        self.username = username
        self.db_connection = mysql.connector.connect(
            host="localhost",          
            user="root",               
            password="123456",      
            database="juegokea"
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
        
        # Retorna las fechas y puntuaciones separadas
        fechas = [partida[0] for partida in partidas]
        puntuaciones = [partida[1] for partida in partidas]
        return fechas, puntuaciones
    
    def dibujar_grafica(self):
        # Obtener las ultimas 10 partidas y sus puntuaciones
        fechas, puntuaciones = self.obtener_ultimas_partidas()
        
        # Si no hay partidas, muestra un mensaje
        if not fechas:
            print(f"No se encontraron partidas para el jugador {self.username}.")
            return
        
        # Graficar
        plt.figure(figsize=(10, 6))
        plt.plot(fechas, puntuaciones, marker='o', color='b', linestyle='-', markersize=6, label="Puntuacion")
        plt.xlabel('Fecha de la Partida')
        plt.ylabel('Puntuacion')
        plt.title(f'Ultimas 10 partidas de {self.username}')
        plt.xticks(rotation=45)  # Rota las fechas para que aparezcan en orden cronologico.
        plt.grid(True)
        plt.tight_layout()
        plt.legend()

        # Guardar grafica como una
        plt.savefig(f'{self.username}_grafica.png')  # Cambia el nombre del archivo al del usuario.
        print(f"Grafica guardada como {self.username}_grafica.png")
        
        plt.show()
