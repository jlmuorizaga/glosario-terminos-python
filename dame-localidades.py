import os
import requests
import psycopg2
from datetime import datetime

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
total=0;
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
    
# Función para obtener las localidades de un municipio
def obtener_localidades(id_estado,id_municipio):
    url_localidades="https://gaia.inegi.org.mx/wscatgeo/v2/localidades/"+id_estado+id_municipio
    #url_municipios = f"https://api.example.com/estados/{id_estado}/municipios"  # URL de ejemplo del servicio de municipios
    respuesta = requests.get(url_localidades)
    
    if respuesta.status_code == 200:
        return respuesta.json().get('datos', [])  # Suponemos que devuelve una lista de localidades
    else:
        print(f"Error al obtener localidades para el municipio {id_estado} {id_municipio}: {respuesta.status_code}")
        return []



limpiar_pantalla()
cursor = conexion.cursor()
print ("**************************************")
print("Fecha y hora inicio:", datetime.now())
print ("**************************************")

# Obtener los estados desde el primer servicio
estados = obtener_estados()
contador=0;
total=0;

# Recorrer los estados y hacer inserciones
for estado in estados:
    #nombre_estado = estado['nombre']  # Suponemos que el JSON tiene el campo 'nombre'
    
    # Insertar el estado en la tabla 'estados'
    #cursor.execute('INSERT INTO estados (nombre) VALUES (%s) RETURNING id', (nombre_estado,))
    id_estado = estado['cvegeo']  # Obtener el id del estado insertado
    nomgeo = estado['nomgeo']

    #print(nomgeo, end=" ")
    print (id_estado+'. '+nomgeo)
 
    

    #print('id_estado=',id_estado)
    #print('nomgeo=',nomgeo)
    
    # Obtener los municipios del estado desde el segundo servicio
    municipios = obtener_municipios(id_estado)
    
    for municipio in municipios:
        cvegeo = municipio['cvegeo']
        cve_ent = municipio['cve_ent']
        cve_mun = municipio['cve_mun']
        #print (municipio)



        localidades=obtener_localidades(cve_ent,cve_mun)
        for localidad in localidades:
            cvegeo = localidad['cvegeo']
            cve_ent = localidad['cve_ent']
            cve_mun = localidad['cve_mun']
            cve_loc = localidad['cve_loc']
            nomgeo =  localidad['nomgeo']
            ambito = localidad['ambito']
            latitud = localidad['latitud']
            longitud = localidad['longitud']
            altitud = localidad['altitud']
            #pob_total = localidad['pob_total']
            #total_viviendas_habitadas = localidad['total_viviendas_habitadas']
            #cve_carta = localidad['cve_carta']
            #if cve_carta is None or cve_carta == "":
            #    cve_carta = 'Empty'
            #estatus = localidad['estatus']
            #periodo = localidad['periodo']
            total=+1
            #print (localidad)
            cursor.execute('INSERT INTO public.localidades(cvegeo, cve_ent, cve_mun, cve_loc,nomgeo,ambito,latitud,longitud,altitud) '
                        +'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) '
                       +'RETURNING cvegeo',(cvegeo, cve_ent, cve_mun, cve_loc, nomgeo, ambito, latitud,longitud, altitud));

        #INSERT INTO public.localidades_p(
	    #cvegeo, cve_ent, cve_mun, cve_loc, nomgeo, ambito, latitud, longitud, altitud, pob_total, total_viviendas_habitadas, cve_carta, estatus, periodo)
	    #VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            


# Confirmar las inserciones en la base de datos
conexion.commit()

# Cerrar la conexión
cursor.close()
conexion.close()
print ("**************************************")
print("Fecha y hora fin: ",  datetime.now())
print ("**************************************")
print("Localidades insertadas correctamente.")
print("Total localidades=",total)