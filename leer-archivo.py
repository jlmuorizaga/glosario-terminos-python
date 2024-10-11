import os  # Asegúrate de importar el módulo os
import re  # Importar el módulo de expresiones regulares
import csv

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Abrir el archivo que contiene la lista de nombres de otros archivos
limpiar_pantalla();

datos_procesados = []

with open('GlosarioTerminos-insumos/letras.txt', 'r') as archivo_principal:
#with open('GlosarioTerminos-insumos/letras-a.txt', 'r') as archivo_principal:
    
    for nombre_archivo in archivo_principal:
        nombre_archivo = nombre_archivo.strip()  # Elimina posibles saltos de línea o espacios
        print(nombre_archivo)

        # Leer el contenido de cada archivo listado
        try:
            
            ruta = os.path.join('GlosarioTerminos-insumos', nombre_archivo)
            # Leer el archivo
            print ('ruta=',ruta)
            with open(ruta, 'r', encoding='utf-8') as archivo_individual:
            #with open(ruta, 'r') as archivo_individual:
            #with open('GlosarioTerminos-insumos/'+nombre_archivo, 'r') as archivo_individual:
                contenido = archivo_individual.read()  # Leer el contenido completo del archivo       
                print(f"Contenido de: {nombre_archivo}:")
                nombre_sin_extension, extension = os.path.splitext(nombre_archivo)
                print("Nombre sin extensión: ",nombre_sin_extension)
                print("*" * 100)  # Separador visual entre archivos

                

            # Iterar sobre cada línea en el contenido
            for linea in contenido.splitlines():
                #print ('Linea= '+linea)
            # Expresión regular para capturar los datos antes del punto y los números después
                resultado = re.search(r'^(.*)\.(\d+)$', linea)
                if resultado:
                    datos = resultado.group(1)  # Captura los datos antes del punto

                    print ('Registro completo:')
                    print (datos)
                    print("-" * 100)  # Separador visual entre archivos
                    partes = datos.split('.', 1)  # Divide en el primer punto
                    if len(partes) > 1:
                        datos_limpios = partes[1].strip()  # Elimina los espacios en blanco al inicio
                        #print("Datos limpios:") 
                        #print (datos_limpios);
                        #print("-" * 100)  # Separador visual entre archivos
                        numero = resultado.group(2)  # Captura el número después del punto
                        print ('numero=',numero)
                        print("-" * 100)  # Separador visual entre archivos
                        concepto, definicion = datos_limpios.split(':', 1)  # Divide en el primer ":"
                        concepto = concepto.strip()  # Elimina posibles espacios alrededor del concepto
                        definicion = definicion.strip()  # Elimina posibles espacios alrededor de la definición
                        print("Concepto:")
                        print(concepto)
                        print("-" * 100)  # Separador visual entre archivos
                        print("Definición:")
                        print (definicion)
                        print("-" * 100)  # Separador visual entre archivos

                        #with open('GlosarioTerminos-insumos/letras-a.txt', 'r') as archivo_principal:                        
                        #print ('Creo que después de aqui envia un error')
                        nombre_archivo_fuente=nombre_sin_extension+"-fuente.txt"
                        try:
                            ruta_fuente = os.path.join('GlosarioTerminos-insumos', nombre_archivo_fuente)
                            print ('ruta_fuente='+ruta_fuente)
                            with open(ruta_fuente, 'r', encoding='utf-8') as archivo_individual_fuente:
                                contenido_fuente = archivo_individual_fuente.read()  # Leer el contenido completo del archivo  
                                # Expresión regular para extraer número, definición y URLs (si existen)
                                patron = r'(\d+)\.\s*(.*?)(?:\s*Sitio web:\s*(.+))?$'
                                # Procesar el texto por líneas
                                for linea_fuente in contenido_fuente.split("\n"):
                                    # Buscar coincidencias por línea
                                    coincidencia = re.match(patron, linea_fuente.strip())
                                    if coincidencia:
                                        numero_fuente = coincidencia[1]  # El número del registro
                                        definicion_fuente = coincidencia[2].strip()  # La definición completa
                                        sitios_web_fuente = coincidencia[3] if coincidencia[3] else ""  # Sitios web (si existen)        
                                        # Si hay sitios web, extraerlos en una lista
                                        urls = re.findall(r'https?://[^\s]+', sitios_web_fuente) if sitios_web_fuente else []
                                        # Mostrar resultados
                                        if (numero==numero_fuente):
                                            print(f"Número: {numero}")
                                            definicion=definicion+"\n\n"
                                            definicion=definicion+'Fuente: \n'+definicion_fuente+"\n\n"
                                            if urls:
                                                definicion=definicion+"Sitio(s) web:\n"
                                                print("Sitio(s) web:")  # Título para los sitios web
                                                for url in urls:
                                                    definicion=definicion+url+"\n"
                                                    print(f"{url}")  # Cada URL en una línea nueva
                                            else:
                                                definicion=definicion+"Sitio(s) web: \nNo hay URLs\n"
                                                print("Sitios web: No hay URLs\n\n")
                                            #definicion=definicion+f"Sitio(s) web: {urls if urls else 'No hay URLs'}"
                                            print(f"Definición: {definicion}")
                                            #print(f"Sitio(s) web: {urls if urls else 'No hay URLs'}")
                                            #print({'Sitios web: '+urls if urls else 'No hay URLs'})
                                            print("-" * 50)
                        except FileNotFoundError:
                            print(f"Error linea 97: {nombre_archivo_fuente} no se encuentra.")


                        
                        # Definir los encabezados
                        encabezados = ["Concepto", "Definición"]
                        # Definir la primer letra de la definición en mayúsculas
                        datos_procesados.append([concepto, definicion[0].upper()+definicion[1:]])
                        #datos_procesados.append([concepto, definicion])

                        # Abrir un archivo CSV para escribir los datos procesados
                        #with open('glosario.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
                        with open('glosario.csv', 'w',newline='') as archivo_csv:
                            escritor_csv = csv.writer(archivo_csv)
                            # Escribir los encabezados
                            escritor_csv.writerow(encabezados)                            
                           # Escribir los datos procesados
                            escritor_csv.writerows(datos_procesados)


                    #print('Datos=>', datos)   

                #print(contenido)
                print("*" * 100)  # Separador visual entre archivos
        except FileNotFoundError:
            print(f"Error linea 119: {nombre_archivo} no se encuentra.")

