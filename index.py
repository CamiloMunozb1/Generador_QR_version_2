from QR_funcion.ingreso_usuario import ConexionDB, IngresoUsuarios
from QR_funcion.generador_qr import ConexionDB, GeneradorQR


ruta_db = "C:/Users/POWER/QR_user.db"
conexion = ConexionDB(ruta_db)

while True:
    print("""
            Bienvenido al generador de QR
            1. Ingresar usuario.
            2. Generar QR.
            3. Guardar nombre del QR.
            4. Mostrar QR.
            5. Salir
        """)
    try:
        usuario = int(input("Ingresa una opcion: "))
        if usuario == 1:
            ingreso_usuario = IngresoUsuarios(conexion)
            ingreso_usuario.ingreso_usuario()
        elif usuario == 2:
            generar_qr = GeneradorQR(conexion)
            generar_qr.codigo_db()
        elif usuario == 3:
            print("Proxima funcion.")
        elif usuario == 4:
            print("Proxima funcion.")
        elif usuario == 5:
            print("Saliendo del programa, gracias por visitarnos.")
            break
        else:
            print("opcion no valida, por favor intentalo con valores del 1 al 5.")
    except ValueError:
        print("Por favor ingresa un valor numerico.")