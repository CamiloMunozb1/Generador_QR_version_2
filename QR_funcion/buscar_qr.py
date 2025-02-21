import sqlite3
from PIL import Image
import os


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

class BuscarQR:
    def __init__(self,conexion):
        self.conexion = conexion

    def busqueda_qr(self):
        try:
            nombre_archivo = str(input("Ingresa el nombre del archivo a buscar: "))
            self.conexion.cursor.execute("SELECT nombre_QR FROM nombres_qr WHERE nombre_QR = ?", (nombre_archivo,))
            resultado = self.conexion.cursor.fetchall()
            if resultado:
                print(f"El archivo {nombre_archivo} fue encontrado.")
                self.abrir_qr(nombre_archivo)
            else:
                print(f"El archivo {nombre_archivo} no fue encontrado.")
        except Exception as error:
            print(f"Error en la busqueda: {error}.")
        except ValueError:
            print("Por favor ingresa un formato valido.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")

    def abrir_qr(self, nombre_archivo):
        try:
            ruta_archivo = f"{nombre_archivo}.png"
            if os.path.exists(ruta_archivo):
                print("Abriendo archivo...")
                imagen = Image.open(ruta_archivo)
                imagen.show()
        except Exception as error:
            print(f"Error al abrir el archivo: {error}.")


ruta = "C:/Users/POWER/QR_user.db"
conexion = ConexionDB(ruta)