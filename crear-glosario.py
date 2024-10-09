import os  # Asegúrate de importar el módulo os
import re  # Importar el módulo de expresiones regulares
import csv

##################################################################################
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
##################################################################################

##################################################################################
def lee_archivo_fuentes():
    with open('GlosarioTerminos-insumos/fuente2.txt', 'r') as archivo_fuente:
        for nombre_archivo_fuente in archivo_fuente:
            # Elimina posibles saltos de línea o espacios
            nombre_archivo_fuente = nombre_archivo_fuente.strip()  
            print('Archivo fuente con extensión:',nombre_archivo_fuente)
            leer_contenido_archivo_letra(nombre_archivo_fuente)
##################################################################################

##################################################################################3
def leer_archivo_letras():
    with open('GlosarioTerminos-insumos/letras-a.txt', 'r') as archivo_principal:
        for nombre_archivo_letra in archivo_principal:
            # Elimina posibles saltos de línea o espacios
            nombre_archivo_letra = nombre_archivo_letra.strip()  
            print('Archivo con extensión:',nombre_archivo_letra)
            leer_contenido_archivo_letra(nombre_archivo_letra)
##################################################################################

##################################################################################
def leer_contenido_archivo_letra(nombre_archivo):
    try:            
        ruta = os.path.join('GlosarioTerminos-insumos', nombre_archivo)
        # Leer el archivo
        #print ('ruta=',ruta)
        with open(ruta, 'r', encoding='utf-8') as archivo_individual:
            contenido = archivo_individual.read()  # Leer el contenido completo del archivo       
            #print(f"Contenido de: {nombre_archivo}:")
            
            nombre_sin_extension, extension = os.path.splitext(nombre_archivo)
            print(f"Nombre sin extensión: {nombre_sin_extension}")
            print("*" * 100)  # Separador visual entre archivos
            # Iterar sobre cada línea en el contenido
            for linea in contenido.splitlines():
        #         #print ('Linea= '+linea)
        #     # Expresión regular para capturar los datos antes del punto y los números después
                 resultado = re.search(r'^(.*)\.(\d+)$', linea)
                 if resultado:
                     datos = resultado.group(1)  # Captura los datos antes del punto

                     #print ('Registro completo:')
                     #print (datos)
                     #print("-" * 100)  # Separador visual entre archivos
                     partes = datos.split('.', 1)  # Divide en el primer punto
                     if len(partes) > 1:
                         datos_limpios = partes[1].strip()  # Elimina los espacios en blanco al inicio
        #                 #print("Datos limpios:") 
        #                 #print (datos_limpios);
        #                 #print("-" * 100)  # Separador visual entre archivos
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
    except FileNotFoundError:
        print(f"Error: {nombre_archivo} no se encuentra.")
    
##################################################################################

limpiar_pantalla();
leer_archivo_letras();
lee_archivo_fuentes();

# Abrir el archivo que contiene la lista de nombres de otros archivos
# datos_procesados = []
# with open('GlosarioTerminos-insumos/letras.txt', 'r') as archivo_principal:
#     for nombre_archivo in archivo_principal:
#         nombre_archivo = nombre_archivo.strip()  # Elimina posibles saltos de línea o espacios
#         print(nombre_archivo)

        # # Leer el contenido de cada archivo listado
        # try:
            
        #     ruta = os.path.join('GlosarioTerminos-insumos', nombre_archivo)
        #     # Leer el archivo
        #     print ('ruta=',ruta)
        #     with open(ruta, 'r', encoding='utf-8') as archivo_individual:
        #     #with open(ruta, 'r') as archivo_individual:
        #     #with open('GlosarioTerminos-insumos/'+nombre_archivo, 'r') as archivo_individual:
        #         contenido = archivo_individual.read()  # Leer el contenido completo del archivo       
        #         print(f"Contenido de: {nombre_archivo}:")
        #         nombre_sin_extension, extension = os.path.splitext(nombre_archivo)
        #         print(f"Nombre sin extensión: {nombre_sin_extension}")
        #         print("*" * 100)  # Separador visual entre archivos

                

        #     # Iterar sobre cada línea en el contenido
        #     for linea in contenido.splitlines():
        #         #print ('Linea= '+linea)
        #     # Expresión regular para capturar los datos antes del punto y los números después
        #         resultado = re.search(r'^(.*)\.(\d+)$', linea)
        #         if resultado:
        #             datos = resultado.group(1)  # Captura los datos antes del punto

        #             print ('Registro completo:')
        #             print (datos)
        #             print("-" * 100)  # Separador visual entre archivos
        #             partes = datos.split('.', 1)  # Divide en el primer punto
        #             if len(partes) > 1:
        #                 datos_limpios = partes[1].strip()  # Elimina los espacios en blanco al inicio
        #                 #print("Datos limpios:") 
        #                 #print (datos_limpios);
        #                 #print("-" * 100)  # Separador visual entre archivos
        #                 numero = resultado.group(2)  # Captura el número después del punto
        #                 print ('numero=',numero)
        #                 print("-" * 100)  # Separador visual entre archivos
        #                 concepto, definicion = datos_limpios.split(':', 1)  # Divide en el primer ":"
        #                 concepto = concepto.strip()  # Elimina posibles espacios alrededor del concepto
        #                 definicion = definicion.strip()  # Elimina posibles espacios alrededor de la definición
        #                 print("Concepto:")
        #                 print(concepto)
        #                 print("-" * 100)  # Separador visual entre archivos
        #                 print("Definición:")
        #                 print (definicion)
        #                 print("-" * 100)  # Separador visual entre archivos
                        
        #                 # Definir los encabezados
        #                 encabezados = ["Concepto", "Definición"]
        #                 # Definir la primer letra de la definición en mayúsculas
        #                 #datos_procesados.append([concepto, definicion[0].upper()+definicion[1:]])
        #                 datos_procesados.append([concepto, definicion])

        #                 # Abrir un archivo CSV para escribir los datos procesados
        #                 #with open('glosario.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
        #                 with open('glosario.csv', 'w',newline='') as archivo_csv:
        #                     escritor_csv = csv.writer(archivo_csv)
        #                     # Escribir los encabezados
        #                     escritor_csv.writerow(encabezados)                            
        #                    # Escribir los datos procesados
        #                     escritor_csv.writerows(datos_procesados)


        #             #print('Datos=>', datos)   

        #         #print(contenido)
        #         print("*" * 100)  # Separador visual entre archivos
        # except FileNotFoundError:
        #     print(f"Error: {nombre_archivo} no se encuentra.")

