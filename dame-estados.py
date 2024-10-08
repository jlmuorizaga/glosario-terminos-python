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
CREATE TABLE IF NOT EXISTS public.mgee
(
    cvegeo character varying(2) COLLATE pg_catalog."default" NOT NULL,
    cve_ent character varying(2) COLLATE pg_catalog."default" NOT NULL,
    nomgeo character varying(50) COLLATE pg_catalog."default" NOT NULL,
    nom_abrev character varying(10) COLLATE pg_catalog."default" NOT NULL,
    pob_total integer NOT NULL,
    pob_femenina integer NOT NULL,
    pob_masculina integer NOT NULL,
    total_viviendas_habitadas integer NOT NULL,
    CONSTRAINT mgee_pkey PRIMARY KEY (cvegeo)
)
'''

# Ejecutar la creación de la tabla
cursor.execute(crear_tabla_sql)
conexion.commit()

# URL de ejemplo con datos JSON
url = "https://gaia.inegi.org.mx/wscatgeo/v2/mgee/"

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
        cvegeo = registro['cvegeo']
        cve_ent = registro['cve_ent']
        nomgeo = registro['nomgeo']
        nom_abrev = registro['nom_abrev']
        pob_total = registro['pob_total']
        pob_femenina = registro['pob_femenina']
        pob_masculina = registro['pob_masculina']
        total_viviendas_habitadas = registro['total_viviendas_habitadas']
        
        # Insertar los datos en la tabla 'usuarios'
        insertar_sql = '''
        INSERT INTO public.mgee(cvegeo, cve_ent, nomgeo, nom_abrev, pob_total, pob_femenina, pob_masculina, total_viviendas_habitadas)
	    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        '''
        
        # Ejecutar la inserción
        cursor.execute(insertar_sql, (cvegeo, cve_ent, nomgeo, nom_abrev, pob_total, pob_femenina, pob_masculina, total_viviendas_habitadas))
    
    # Confirmar las inserciones
    conexion.commit()

    print("Datos insertados correctamente en la tabla 'mgee_p'.")
else:
    print(f"Error al hacer la solicitud: {respuesta.status_code}")

# Cerrar la conexión
cursor.close()
conexion.close()
