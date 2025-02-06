from CrearGrafica import CrearGrafica


class Main:
    def __init__(self, username):
        self.username = username
    
    def ejecutar(self):
        grafica = CrearGrafica(self.username)
        grafica.dibujar_grafica()


if __name__ == "__main__":
    username = "juan123"  # Cambiar por el nombre de usuario deseado
    main = Main(username)
    main.ejecutar()

