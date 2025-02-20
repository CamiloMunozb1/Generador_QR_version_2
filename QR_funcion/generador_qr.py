from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import qrcode
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

class GeneradorQR:
    def __init__(self, conxion):
        self.conexion = conxion
    def generar_qr(self, link_usuario, mensaje_qr):
        try:
            img = qrcode.make(link_usuario)
            new_image = Image.new("RGB",(img.size[0],img.size[0]+50),"white")
            font = ImageFont.load_default()
            draw = ImageDraw.Draw(new_image)
            text_size = draw.textbbox((0,0), mensaje_qr, font=font)
            text_x = (img.size[0] - (text_size[2] - text_size[0])) // 2
            text_y = img.size[1] + 10
            draw.text((text_x, text_y), mensaje_qr, font=font, fill="black")
            buffer = BytesIO()
            new_image.save(buffer, format="PNG")
            return buffer.getvalue()
        except Exception as error:
            print(f"Error al generar el codigo QR, volver a intentar: {error}.")
            return None

    def codigo_db(self):
        try:
            nombre_qr = str(input("Ingresa el titulo del QR: "))
            nombre_usuario = str(input("Ingresa el nombre del usuario: "))
            apellido_usuario = str(input("Ingresa el apellido del usuario: "))
            link_usuario = str(input("Ingresa el link para generar el codigo QR: "))
            mensaje_qr = str(input("Ingresa el mensaje para el codigo QR: "))
            self.conexion.cursor.execute("SELECT usuario_id FROM usuario_qr WHERE nombre_usuario = ? AND apellido_usuario = ?", (nombre_usuario, apellido_usuario))
            usuario = self.conexion.cursor.fetchone()
            if usuario:
                usuario_id = usuario[0] 
                qr_binario = self.generar_qr(link_usuario, mensaje_qr)
                if qr_binario:
                    self.conexion.cursor.execute("INSERT INTO nombres_qr (nombre_qr,imagen_QR, usuario_id) VALUES (?,?,?)",(nombre_qr, qr_binario, usuario_id))
                    self.conexion.conn.commit()
                    print("QR guardado correctamente.")
                else:
                    print("Error al guardar el QR, no se guardara en la base de datos.")
            else:
                print("Usuario no encontrado.")
        except ValueError:
            print("Error al guardar el QR, volver a intentar.")
        except sqlite3.Error as error:
            print(f"Error al guardar el QR: {error}.")