# Abrir el archivo en modo lectura ('r')
#with open('GlosarioTerminos-insumos\letras.txt', 'r') as archivo:
#    letra = archivo.read()  # Lee todo el contenido del archivo
#    with open(letra, 'r') as archivo-letra:
#        contenido=archivo-letra.read()
#        print(contenido)  # Imprime el contenido

# Abrir el archivo que contiene la lista de nombres de otros archivos
with open('GlosarioTerminos-insumos\letras.txt', 'r') as archivo_principal:
    for nombre_archivo in archivo_principal:
        nombre_archivo = nombre_archivo.strip()  # Elimina posibles saltos de línea o espacios

        # Leer el contenido de cada archivo listado
        try:
            with open('GlosarioTerminos-insumos\\'+nombre_archivo, 'r') as archivo_individual:
                contenido = archivo_individual.read()  # Leer el contenido completo del archivo
                print(f"Contenido de {nombre_archivo}:")
                print(contenido)
                print("-" * 50)  # Separador visual entre archivos
        except FileNotFoundError:
            print(f"Error: {nombre_archivo} no se encuentra.")

