import os
import requests
import json
import psycopg2

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Conexión a la base de datos PostgreSQL
conexion = psycopg2.connect(
    host="localhost",
    database="catalogo_unico",
    user="postgres",
    password="postgres",
    port="5432"  # Puerto predeterminado de PostgreSQL
)

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear la tabla (si no existe)
crear_tabla_sql = '''
CREATE TABLE IF NOT EXISTS public.cat_tipo_asen
(
    cve_tipo_asen numeric(2,0) NOT NULL,
    descripcion character varying(21) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT cve_tipo_asen_pk PRIMARY KEY (cve_tipo_asen)
)
'''

# Ejecutar la creación de la tabla
cursor.execute(crear_tabla_sql)
conexion.commit()

# URL de ejemplo con datos JSON
url = "https://gaia.inegi.org.mx/wscatgeo/v2/catasentamientos"

# Hacemos la solicitud al servicio
respuesta = requests.get(url)

# Verificamos que la solicitud haya sido exitosa
if respuesta.status_code == 200:
    # Convertimos la respuesta en un diccionario Python
    datos = respuesta.json()
    ## datos_str=json.loads(datos)
    
    # Limpiar la pantalla antes de mostrar los resultados
    limpiar_pantalla()
    datos_formateados = json.dumps(datos, indent=4)
    print(datos_formateados)
    
    # Recorremos cada usuario del JSON y lo insertamos en la tabla
    
    for registro in datos['datos']:
        cve_tipo_asen = registro['cve_tipo_asen']
        descripcion = registro['descripcion']
        
        # Insertar los datos en la tabla 'usuarios'
        insertar_sql = '''
        INSERT INTO public.cat_tipo_asen(cve_tipo_asen, descripcion) VALUES (%s, %s);
        '''
        
        # Ejecutar la inserción
        cursor.execute(insertar_sql, (cve_tipo_asen, descripcion))
    
    # Confirmar las inserciones
    conexion.commit()

    print("Datos insertados correctamente en la tabla 'cat_tipo_asen'.")
else:
    print(f"Error al hacer la solicitud: {respuesta.status_code}")

# Cerrar la conexión
cursor.close()
conexion.close()
