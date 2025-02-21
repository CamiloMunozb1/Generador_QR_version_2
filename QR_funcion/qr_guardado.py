import sqlite3
import pandas as pd


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


class MostarQR:
    def __init__(self,conexion):
        self.conexion = conexion
    
    def archivos_guardados(self):
        try:
            query = "SELECT nombre_QR FROM nombres_qr"
            resultado_df = pd.read_sql_query(query, self.conexion.conn)
            if not resultado_df.empty:
                print(resultado_df)
            else:
                print("No hay archivos guardados en la base de datos.")
        except Exception as error:
            print(f"Error en la busqueda: {error}.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")


ruta = "C:/Users/POWER/QR_user.db"
conexion = ConexionDB(ruta)