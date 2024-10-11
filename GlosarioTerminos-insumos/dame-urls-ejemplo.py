import re

# Simulación del contenido de un archivo de texto
texto = """
48. Gobierno del Municipio de Benito Juárez del Estado de Quintana Roo. Programa de Desarrollo Urbano del Centro de Población Cancún 2014-2030. Sitio web: http://seduvi.qroo.gob.mx/pdus/36-PDU%20DEL%20CENTRO%20DE%20POBLACION%20CANCUN%20BENITO%20JUAREZ%20QUINTANA%20ROO%202014-2030(1).pdf

49. Definición realizada con base en los conceptos contemplados en las páginas de internet: Sitio web: http://www.infoagro.com/diccionario_agricola/traducir.asp?i=1&id=227&idt=1&palabra=cultivo__cultivo_cultivos_ https://deconceptos.com/ciencias-sociales/cultivo

50. Instituto Nacional de Estadística y Geografía. (1998). Diccionario de Datos Topográficos Esc. 1:250 000. México: INEGI.
"""

# Expresión regular para extraer número, definición y URLs (si existen)
patron = r'(\d+)\.\s*(.*?)(?:\s*Sitio web:\s*(.+))?$'

# Procesar el texto por líneas
for linea in texto.split("\n"):
    # Buscar coincidencias por línea
    coincidencia = re.match(patron, linea.strip())
    if coincidencia:
        numero = coincidencia[1]  # El número del registro
        definicion = coincidencia[2].strip()  # La definición completa
        sitios_web = coincidencia[3] if coincidencia[3] else ""  # Sitios web (si existen)
        
        # Si hay sitios web, extraerlos en una lista
        urls = re.findall(r'https?://[^\s]+', sitios_web) if sitios_web else []

        # Mostrar resultados
        #if (numero=='50'):
        print(f"Número: {numero}")
        print(f"Definición: {definicion}")
        print(f"Sitios web: {urls if urls else 'No hay URLs'}")
        #print({'Sitios web: '+urls if urls else 'No hay URLs'})
        print("-" * 50)
