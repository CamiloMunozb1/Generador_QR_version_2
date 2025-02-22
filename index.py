# Importamos las clases necesarias desde diferentes módulos dentro de la carpeta QR_funcion.
from QR_funcion.generador_qr import ConexionDB, GeneradorQR
from QR_funcion.buscar_qr import ConexionDB, BuscarQR
from QR_funcion.qr_guardado import ConexionDB, MostarQR
from QR_funcion.eliminacion_qr import ConexionDB, EliminarQR

# Definimos la ruta de la base de datos donde se almacenarán los nombres de los códigos QR.
ruta_db = "C:/Users/POWER/QR_user.db"

# Creamos una instancia de la conexión a la base de datos.
conexion = ConexionDB(ruta_db)

# Iniciamos un bucle infinito para mostrar el menú hasta que el usuario decida salir.
while True:
    print("""
            Bienvenido al generador de QR
            1. Generar QR.
            2. Mostrar QR.
            3. Mostrar los nombres de los QR's en la base de datos.
            4. Eliminar QR de la base de datos y del sistema.
            5. Salir
        """)
    try:
        # Solicitamos al usuario que ingrese una opción.
        usuario = int(input("Ingresa una opcion: "))

        # Opción 1: Generar un nuevo código QR.
        if usuario == 1:
            generar_qr = GeneradorQR(conexion)  # Instanciamos la clase para generar QR.
            generar_qr.generar_qr()  # Llamamos al método que genera el QR.

        # Opción 2: Buscar y abrir un QR existente.
        elif usuario == 2:
            busqueda_qr = BuscarQR(conexion)  # Instanciamos la clase de búsqueda de QR.
            nombre_qr = busqueda_qr.busqueda_qr()  # Obtenemos el nombre del QR buscado.
            if nombre_qr:  # Si el QR existe, lo abrimos.
                busqueda_qr.abrir_qr(nombre_qr)

        # Opción 3: Mostrar los nombres de los QR guardados en la base de datos.
        elif usuario == 3:
            mostrar_qr = MostarQR(conexion)  # Instanciamos la clase para mostrar QR.
            mostrar_qr.archivos_guardados()  # Mostramos la lista de QR guardados.

        # Opción 4: Eliminar un QR de la base de datos y del sistema.
        elif usuario == 4:
            elimnar_qr = EliminarQR(conexion)  # Instanciamos la clase de eliminación.
            nombre_archivo = elimnar_qr.eliminar_qr_db()  # Eliminamos el QR de la base de datos.
            if nombre_archivo:  # Si existe en el sistema, lo eliminamos también.
                elimnar_qr.eliminar_qr_sistema(nombre_archivo)

        # Opción 5: Salir del programa.
        elif usuario == 5:
            print("Saliendo del programa...")
            break  # Rompemos el bucle y terminamos la ejecución.

        # Si el usuario ingresa un número fuera del rango permitido.
        else:
            print("Opción no válida, por favor intenta con valores del 1 al 5.")

    # Capturamos el error si el usuario ingresa un valor no numérico.
    except ValueError:
        print("Por favor ingresa un valor numérico.")

    # Capturamos cualquier otro error inesperado.
    except Exception as error:
        print(f"Error en el programa: {error}.")
