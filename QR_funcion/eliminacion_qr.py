# Importamos las librerías necesarias
import sqlite3  # Para manejar la base de datos SQLite
import os  # Para manejar archivos en el sistema


# CLASE PARA MANEJAR LA CONEXIÓN A LA BASE DE DATOS
class ConexionDB:
    def __init__(self, base_db):
        try:
            # Establecemos la conexión con la base de datos SQLite
            self.conn = sqlite3.connect(base_db)
            self.cursor = self.conn.cursor()  # Creamos un cursor para ejecutar consultas
        except sqlite3.Error as error:
            # Capturamos cualquier error que ocurra en la conexión a la base de datos
            print(f"Error en la base de datos: {error}.")

    def cierre_base(self):
        # Cierra la conexión con la base de datos
        self.conn.close()
        print("Conexion cerrada.")


# CLASE PARA ELIMINAR CÓDIGOS QR DE LA BASE DE DATOS Y DEL SISTEMA
class EliminarQR:
    def __init__(self, conexion):
        # Recibe una instancia de la conexión a la base de datos
        self.conexion = conexion

    def eliminar_qr_db(self):
        try:
            # Solicita el nombre del archivo a eliminar
            nombre_archivo = str(input("Ingresa el nombre del qr a eliminar de la base y del sistema: ")).strip()

            # Pide confirmación antes de eliminar el QR
            confirmacion = str(input(f"¿Estás seguro de eliminar el archivo {nombre_archivo}? (S/N): ")).lower()
            if confirmacion != "s":
                print("Eliminación cancelada.")  # Cancela la operación si el usuario no confirma
                return

            # Busca el ID del QR en la base de datos
            self.conexion.cursor.execute("SELECT QR_ID FROM nombres_QR WHERE nombre_QR = ?", (nombre_archivo,))
            resultado = self.conexion.cursor.fetchone()

            if resultado:
                resultado_id = resultado[0]

                # Elimina el registro de la base de datos
                self.conexion.cursor.execute(
                    "DELETE FROM nombres_qr WHERE nombre_QR = ? AND QR_ID = ?", (nombre_archivo, resultado_id)
                )
                self.conexion.conn.commit()
                print(f"El archivo {nombre_archivo} fue eliminado de la base de datos.")

                # Llama a la función para eliminar el archivo del sistema
                self.eliminar_qr_sistema(nombre_archivo)
            else:
                print(f"El archivo {nombre_archivo} no fue encontrado en la base de datos.")

        except ValueError:
            print("Por favor ingresa un formato valido.")  # Captura errores en la entrada de datos
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")  # Captura errores en la base de datos
        except Exception as error:
            print(f"Error en la eliminacion: {error}.")  # Captura cualquier otro error

    def eliminar_qr_sistema(self, nombre_archivo):
        try:
            # Construimos la ruta del archivo que se quiere eliminar
            ruta_archivo = f"{nombre_archivo}.png"

            # Verificamos si el archivo existe en el sistema
            if os.path.exists(ruta_archivo):
                os.remove(ruta_archivo)  # Eliminamos el archivo
                print(f"El archivo {nombre_archivo} fue eliminado del sistema.")
            else:
                print(f"El archivo {nombre_archivo} no fue encontrado en el sistema.")

        except Exception as error:
            print(f"Error al eliminar el archivo: {error}.")  # Captura cualquier error en la eliminación


# Definimos la ruta de la base de datos
ruta = "C:/Users/POWER/QR_user.db"

# Creamos una instancia de la conexión a la base de datos
conexion = ConexionDB(ruta)
