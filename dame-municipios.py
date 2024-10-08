import os
import requests
import psycopg2

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

    # Conexión a PostgreSQL
conexion = psycopg2.connect(
    host="localhost",
    database="catalogo_unico",
    user="postgres",
    password="postgres",
    port="5432"  # Puerto predeterminado de PostgreSQL
)

# Función para obtener los estados
def obtener_estados():
    url_estados = "https://gaia.inegi.org.mx/wscatgeo/v2/mgee/"  # URL de ejemplo del servicio de estados
    respuesta = requests.get(url_estados)
    
    if respuesta.status_code == 200:
        return respuesta.json().get('datos', [])  # Acceder a 'datos' y retornar una lista vacía si no existe
    else:
        print(f"Error al obtener estados: {respuesta.status_code}")
        return []

# Función para obtener los municipios de un estado
def obtener_municipios(id_estado):
    url_municipios="https://gaia.inegi.org.mx/wscatgeo/v2/mgem/"+id_estado 
    #url_municipios = f"https://api.example.com/estados/{id_estado}/municipios"  # URL de ejemplo del servicio de municipios
    respuesta = requests.get(url_municipios)
    
    if respuesta.status_code == 200:
        return respuesta.json().get('datos', [])  # Suponemos que devuelve una lista de municipios
    else:
        print(f"Error al obtener municipios para el estado {id_estado}: {respuesta.status_code}")
        return []

limpiar_pantalla()
cursor = conexion.cursor()

# Obtener los estados desde el primer servicio
estados = obtener_estados()

# Recorrer los estados y hacer inserciones
for estado in estados:
    #nombre_estado = estado['nombre']  # Suponemos que el JSON tiene el campo 'nombre'
    
    # Insertar el estado en la tabla 'estados'
    #cursor.execute('INSERT INTO estados (nombre) VALUES (%s) RETURNING id', (nombre_estado,))
    id_estado = estado['cvegeo']  # Obtener el id del estado insertado
    nomgeo = estado['nomgeo']

    #print('id_estado=',id_estado)
    #print('nomgeo=',nomgeo)
    
    # Obtener los municipios del estado desde el segundo servicio
    municipios = obtener_municipios(id_estado)
    
    for municipio in municipios:
        #print (municipio)

        cvegeo = municipio['cvegeo']
        cve_ent = municipio['cve_ent']
        cve_mun = municipio['cve_mun']
        nomgeo = municipio['nomgeo']
        cve_cab = municipio['cve_cab']
        #pob_total = municipio['pob_total']
        #pob_femenina = municipio['pob_femenina']
        pob_total='0'
        pob_femenina='0'
        #pob_masculina = municipio['pob_masculina']
        pob_masculina = '0'
        #total_viviendas_habitadas = municipio['total_viviendas_habitadas']
        total_viviendas_habitadas = '0'
        # Insertar el municipio en la tabla 'municipios' con el id del estado correspondiente
        #cursor.execute('INSERT INTO estados (nombre) VALUES (%s) RETURNING id', (nombre_estado,))
  
       # cursor.execute('INSERT INTO public.mgem_p(cvegeo, cve_ent, cve_mun, nomgeo, cve_cab, pob_total, pob_femenina, pob_masculina, total_viviendas_habitadas) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) '
       #                +'RETURNING cvegeo',(cvegeo, cve_ent, cve_mun, nomgeo, cve_cab, pob_total, pob_femenina, pob_masculina, total_viviendas_habitadas));
        cursor.execute('INSERT INTO public.mgem(cvegeo, cve_ent, cve_mun, nomgeo,cve_cab, pob_total, pob_femenina, pob_masculina, total_viviendas_habitadas) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s) '
                       +'RETURNING cvegeo',(cvegeo, cve_ent, cve_mun, nomgeo,cve_cab, pob_total,pob_femenina, pob_masculina, total_viviendas_habitadas));

# Confirmar las inserciones en la base de datos
conexion.commit()

# Cerrar la conexión
cursor.close()
conexion.close()

print("Municipios insertados correctamente.")