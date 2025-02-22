# Importamos las librerías necesarias
import sqlite3  # Para manejar la base de datos SQLite
from PIL import Image, ImageDraw, ImageFont  # Para manipular imágenes y agregar texto
import qrcode  # Para generar códigos QR


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


# CLASE PARA GENERAR CÓDIGOS QR
class GeneradorQR:
    def __init__(self, conexion):  
        # Recibe una instancia de la conexión a la base de datos
        self.conexion = conexion

    def generar_qr(self):
        try:
            # Pedimos al usuario la información necesaria
            link_usuario = input("Ingresa el link para generar el código QR: ")
            mensaje_qr = input("Ingresa el mensaje que contendrá el QR: ")
            nombre_archivo = input("Ingresa el nombre del archivo para guardar el QR: ")

            # Insertamos el nombre del QR en la base de datos
            self.conexion.cursor.execute("INSERT INTO nombres_qr (nombre_QR) VALUES (?)", (nombre_archivo,))
            self.conexion.conn.commit()  # Guardamos los cambios en la base de datos

            # Generamos el código QR con el enlace proporcionado
            qr = qrcode.QRCode(box_size=10, border=4)  # Configuración del QR
            qr.add_data(link_usuario)  # Agregamos los datos al QR
            qr.make(fit=True)  # Ajustamos el tamaño automáticamente
            img = qr.make_image(fill="black", back_color="white").convert("RGB")  # Convertimos a imagen RGB

            # Creamos una nueva imagen más grande para incluir texto debajo del QR
            new_image = Image.new("RGB", (img.width, img.height + 50), "white")  # Espacio extra abajo
            new_image.paste(img, (0, 0))  # Pegamos el código QR en la nueva imagen

            # Creamos un objeto de dibujo sobre la nueva imagen
            draw = ImageDraw.Draw(new_image)

            # Cargamos una fuente predeterminada (puede cambiarse a una fuente personalizada si se necesita)
            font = ImageFont.load_default()

            # Dibujamos un rectángulo blanco en la parte inferior (opcional)
            draw.rectangle([(0, img.height), (img.width, img.height + 50)], fill="white")

            # Agregamos el texto ingresado por el usuario en la parte inferior del QR
            draw.text((10, img.height + 10), mensaje_qr, font=font, fill="black")  

            # Guardamos la imagen generada con el nombre proporcionado
            new_image.save(f"{nombre_archivo}.png")
            print("Código QR generado correctamente.")

        except Exception as error:
            print(f"Error al generar el QR: {error}.")  # Manejamos errores generales
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")  # Manejamos errores de base de datos


# Definimos la ruta de la base de datos
ruta = "C:/Users/POWER/QR_user.db"

# Creamos una instancia de la conexión a la base de datos
conexion = ConexionDB(ruta)
