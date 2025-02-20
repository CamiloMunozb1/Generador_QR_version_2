import sqlite3
from PIL import Image, ImageDraw, ImageFont
import qrcode


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

class GeneradorQR:

    def __init__(self, conexion):  
        self.conexion = conexion

    def generar_qr(self):
        try:
            link_usuario = input("Ingresa el link para generar el código QR: ")
            mensaje_qr = input("Ingresa el mensaje que contendrá el QR: ")
            nombre_archivo = input("Ingresa el nombre del archivo para guardar el QR: ")

            self.conexion.cursor.execute("INSERT INTO nombres_qr (nombre_QR) VALUES (?)", (nombre_archivo,))
            self.conexion.conn.commit()

            # Generar QR
            qr = qrcode.QRCode(box_size=10, border=4)
            qr.add_data(link_usuario)
            qr.make(fit=True)
            img = qr.make_image(fill="black", back_color="white").convert("RGB")  # <- Convertir a RGB

            # Crear nueva imagen con más espacio para el texto
            new_image = Image.new("RGB", (img.width, img.height + 50), "white")

            # Pegar la imagen QR en la nueva imagen
            new_image.paste(img, (0, 0))

            # Crear objeto de dibujo
            draw = ImageDraw.Draw(new_image)

            # Cargar una fuente por defecto
            font = ImageFont.load_default()

            # Dibujar el fondo del texto (opcional)
            draw.rectangle([(0, img.height), (img.width, img.height + 50)], fill="white")

            # Agregar el texto con la fuente correcta
            draw.text((10, img.height + 10), mensaje_qr, font=font, fill="black")  

            # Guardar la imagen
            new_image.save(f"{nombre_archivo}.png")
            print("Código QR generado correctamente.")

        except Exception as error:
            print(f"Error al generar el QR: {error}.")


ruta = "C:/Users/POWER/QR_user.db"
conexion = ConexionDB(ruta)