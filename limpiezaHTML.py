import os
from bs4 import BeautifulSoup
import re
import chardet

def obtener_codificacion(ruta_archivo):
    with open(ruta_archivo, 'rb') as archivo_binario:
        resultado = chardet.detect(archivo_binario.read())
    return resultado['encoding']

def limpiar_html(html):
    # Parsear el HTML con BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Eliminar estilos en línea y scripts
    for tag in soup.find_all(['style', 'script']):
        tag.decompose()

    # Eliminar etiquetas de formato
    for tag in soup.find_all(['font', 'span', 'b', 'i']):
        tag.unwrap()

    # Eliminar atributos de estilo, clase y alineación
    for tag in soup():
        tag.attrs = {}  # Elimina todos los atributos

    # Eliminar etiquetas vacías
    for tag in soup.find_all(True):
        if not tag.text.strip():
            tag.decompose()

    # Eliminar espacios innecesarios
    texto_limpio = re.sub(r'\s+', ' ', soup.get_text(separator=' ', strip=True))

    # Conservar títulos y listas
    for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        texto_limpio += tag.prettify()

    return texto_limpio

def procesar_archivos_html(carpeta_entrada, carpeta_salida):
    # Asegurarse de que la carpeta de textos limpios exista
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    # Iterar sobre todos los archivos en la carpeta HTML
    for nombre_archivo in os.listdir(carpeta_entrada):
        ruta_archivo = os.path.join(carpeta_entrada, nombre_archivo)

        # Verificar si el elemento en la carpeta es un archivo
        if os.path.isfile(ruta_archivo):
            # Obtener la codificación del archivo
            codificacion = obtener_codificacion(ruta_archivo)

            with open(ruta_archivo, 'r', encoding=codificacion, errors='replace') as archivo:
                contenido_html = archivo.read()

                # Aplicar la función de limpieza
                html_limpio = limpiar_html(contenido_html)

                # Guardar el HTML limpio en un nuevo archivo
                nombre_salida = os.path.splitext(nombre_archivo)[0] + '_limpio.html'
                ruta_salida = os.path.join(carpeta_salida, nombre_salida)

                with open(ruta_salida, 'w', encoding='utf-8') as archivo_salida:
                    archivo_salida.write(html_limpio)

    print("Proceso completado.")

# Rutas de las carpetas de entrada y salida
carpeta_html_entrada = '/home/dev1/AndroidStudioProjects/procesarDocument/procesadoSentencias/'
carpeta_textos_limpios_salida = '/home/dev1/AndroidStudioProjects/procesarDocument/corteConsHTMLlimpio/sentencias/'

# Procesar archivos HTML
procesar_archivos_html(carpeta_html_entrada, carpeta_textos_limpios_salida)
