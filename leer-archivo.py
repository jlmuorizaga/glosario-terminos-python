import os  # Asegúrate de importar el módulo os
import re  # Importar el módulo de expresiones regulares

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Abrir el archivo que contiene la lista de nombres de otros archivos
limpiar_pantalla();
with open('GlosarioTerminos-insumos/letras.txt', 'r') as archivo_principal:
    for nombre_archivo in archivo_principal:
        nombre_archivo = nombre_archivo.strip()  # Elimina posibles saltos de línea o espacios

        # Leer el contenido de cada archivo listado
        try:
            with open('GlosarioTerminos-insumos/'+nombre_archivo, 'r') as archivo_individual:
                contenido = archivo_individual.read()  # Leer el contenido completo del archivo
                
                print(f"Contenido de: {nombre_archivo}:")
                nombre_sin_extension, extension = os.path.splitext(nombre_archivo)
                print(f"Nombre sin extensión: {nombre_sin_extension}")
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


                    #print('Datos=>', datos)   

                #print(contenido)
                print("*" * 100)  # Separador visual entre archivos
        except FileNotFoundError:
            print(f"Error: {nombre_archivo} no se encuentra.")

