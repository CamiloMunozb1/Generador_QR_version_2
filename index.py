from QR_funcion.generador_qr import ConexionDB, GeneradorQR
#from QR_funcion.mostar_qr import ConexionDB, MostrarQR


ruta_db = "C:/Users/POWER/QR_user.db"
conexion = ConexionDB(ruta_db)

while True:
    print("""
            Bienvenido al generador de QR
            1. Generar QR.
            2. Mostrar QR.
            3. Salir
        """)
    try:
        usuario = int(input("Ingresa una opcion: "))
        if usuario == 1:
            generar_qr = GeneradorQR(conexion)
            generar_qr.generar_qr()
        elif usuario == 2:
            print("Proxima funcion.")
        elif usuario == 3:
            print("Saliendo del programa, gracias por visitarnos.")
            break
        else:
            print("opcion no valida, por favor intentalo con valores del 1 al 5.")
    except ValueError:
        print("Por favor ingresa un valor numerico.")