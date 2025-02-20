from QR_funcion.generador_qr import ConexionDB, GeneradorQR
from QR_funcion.buscar_qr import ConexionDB, BuscarQR
from QR_funcion.qr_guardado import ConexionDB, MostarQR


ruta_db = "C:/Users/POWER/QR_user.db"
conexion = ConexionDB(ruta_db)

while True:
    print("""
            Bienvenido al generador de QR
            1. Generar QR.
            2. Mostrar QR.
            3. Mostar los nombres de los QR's en la base de datos.
            4. Salir
        """)
    try:
        usuario = int(input("Ingresa una opcion: "))
        if usuario == 1:
            generar_qr = GeneradorQR(conexion)
            generar_qr.generar_qr()
        elif usuario == 2:
            busqueda_qr = BuscarQR(conexion)
            nombre_qr = busqueda_qr.busqueda_qr()
            if nombre_qr:
                busqueda_qr.abrir_qr(nombre_qr)
        elif usuario == 3:
            mostrar_qr = MostarQR(conexion)
            mostrar_qr.archivos_guardados()
        elif usuario == 4:
            print("Saliendo del programa, gracias por visitarnos.")
            break
        else:
            print("opcion no valida, por favor intentalo con valores del 1 al 5.")
    except ValueError:
        print("Por favor ingresa un valor numerico.")