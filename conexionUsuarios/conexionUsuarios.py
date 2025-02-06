import mysql.connector


def obtenerUsuario(nombre_usuario):

    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Usuarios"
    )
    cursor = conexion.cursor(dictionary=True)

    consulta = "SELECT * FROM usuarios WHERE nombre_usuario = %s"

    cursor.execute(consulta, (nombre_usuario,))

    usuario = cursor.fetchone()

    cursor.close()
    conexion.close()

    return usuario
