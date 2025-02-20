import sqlite3

class ConexionDB:
    def __init__(self, base_db):
        try:
            self.conn = sqlite3.connect(base_db)
            self.cursor= self.conn.cursor()
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")
    
    def cierre_base(self):
        self.conn.close()
        print("Conexion cerrada.")


class IngresoUsuarios:
    def __init__(self, conexion):
        self.conexion = conexion
    
    def ingreso_usuario(self):
        try:
            nombre_usuario = str(input("Ingresa el nomnbre del usuario: "))
            apellido_usuario = str(input("Ingresa el apellido del usuario: "))
            self.conexion.cursor.execute("INSERT INTO usuario_qr (nombre_usuario, apellido_usuario) VALUES (?,?)", (nombre_usuario, apellido_usuario))
            self.conexion.conn.commit()
            print("Usuario ingresado correctamente.")
        except ValueError:
            print("Error al ingresar al usuario, volver a intentar.")
        except sqlite3.Error as error:
            print(f"Error al ingresar al usuario: {error}.")


ruta = "C:/Users/POWER/QR_user.db"
conexion = ConexionDB(ruta)