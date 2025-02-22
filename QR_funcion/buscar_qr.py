# Importamos las librerías necesarias
import sqlite3  # Para manejar la base de datos SQLite
from PIL import Image  # Para abrir y visualizar imágenes
import os  # Para verificar la existencia de archivos


# CLASE PARA MANEJAR LA CONEXIÓN A LA BASE DE DATOS
class ConexionDB:
    def __init__(self, base_db):
        try:
            # Establecemos la conexión con la base de datos SQLite
            self.conn = sqlite3.connect(base_db)
            self.cursor = self.conn.cursor()  # Creamos un cursor para ejecutar consultas
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")  # Manejamos errores de conexión
    
    def cierre_base(self):
        # Cierra la conexión con la base de datos
        self.conn.close()
        print("Conexión cerrada.")


# CLASE PARA BUSCAR Y ABRIR CÓDIGOS QR GUARDADOS
class BuscarQR:
    def __init__(self, conexion):
        # Recibe una instancia de la conexión a la base de datos
        self.conexion = conexion

    def busqueda_qr(self):
        try:
            # Solicitamos al usuario el nombre del archivo a buscar
            nombre_archivo = str(input("Ingresa el nombre del archivo a buscar: "))

            # Ejecutamos la consulta para verificar si el archivo existe en la base de datos
            self.conexion.cursor.execute("SELECT nombre_QR FROM nombres_qr WHERE nombre_QR = ?", (nombre_archivo,))
            resultado = self.conexion.cursor.fetchall()

            # Si el resultado contiene datos, el archivo existe
            if resultado:
                print(f"El archivo {nombre_archivo} fue encontrado.")
                self.abrir_qr(nombre_archivo)  # Llamamos al método para abrir el archivo
            else:
                print(f"El archivo {nombre_archivo} no fue encontrado en la base de datos.")

        except Exception as error:
            print(f"Error en la búsqueda: {error}.")  # Manejamos errores generales
        except ValueError:
            print("Por favor, ingresa un formato válido.")  # Manejamos errores de tipo
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")  # Manejamos errores de base de datos

    def abrir_qr(self, nombre_archivo):
        try:
            # Definimos la ruta del archivo QR
            ruta_archivo = f"{nombre_archivo}.png"

            # Verificamos si el archivo existe en la carpeta actual
            if os.path.exists(ruta_archivo):
                print("Abriendo archivo...")
                imagen = Image.open(ruta_archivo)  # Abrimos la imagen con PIL
                imagen.show()  # Mostramos la imagen
            else:
                print("El archivo de imagen no existe en el sistema.")

        except Exception as error:
            print(f"Error al abrir el archivo: {error}.")  # Manejamos errores generales


# Definimos la ruta de la base de datos
ruta = "C:/Users/POWER/QR_user.db"

# Creamos una instancia de la conexión a la base de datos
conexion = ConexionDB(ruta)
