import sqlite3  # librería para manejar bases de datos sqlite
import pandas as pd  # librería para manejar datos en formato tabular


class ConexionDB:
    def __init__(self, base_db):
        try:
            # establece la conexión con la base de datos
            self.conn = sqlite3.connect(base_db)
            self.cursor = self.conn.cursor()  # crea un cursor para ejecutar consultas
        except sqlite3.Error as error:
            # muestra un mensaje si hay un error en la conexión
            print(f"error en la base de datos: {error}.")
    
    def cierre_base(self):
        # cierra la conexión con la base de datos
        self.conn.close()
        print("conexion cerrada.")


class MostarQR:
    def __init__(self, conexion):
        # recibe la conexión a la base de datos
        self.conexion = conexion
    
    def archivos_guardados(self):
        try:
            # consulta sql para obtener los nombres de los qr almacenados
            query = "SELECT nombre_QR FROM nombres_qr"
            resultado_df = pd.read_sql_query(query, self.conexion.conn)  # ejecuta la consulta y almacena el resultado en un dataframe
            
            if not resultado_df.empty:
                # si hay resultados, los imprime
                print(resultado_df)
            else:
                # si no hay resultados, muestra un mensaje indicando que no hay archivos guardados
                print("no hay archivos guardados en la base de datos.")
        except Exception as error:
            # maneja errores generales en la consulta
            print(f"error en la busqueda: {error}.")
        except sqlite3.Error as error:
            # maneja errores específicos de sqlite
            print(f"error en la base de datos: {error}.")


ruta = "C:/Users/POWER/QR_user.db"  # ruta de la base de datos
conexion = ConexionDB(ruta)  # crea una instancia de la conexión

