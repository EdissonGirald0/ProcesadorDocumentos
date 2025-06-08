import os
from bs4 import BeautifulSoup
import re
import chardet

def obtener_codificacion(ruta_archivo):
    with open(ruta_archivo, 'rb') as archivo_binario:
        resultado = chardet.detect(archivo_binario.read())
    return resultado['encoding']

def limpiar_html(html):
    """
    Limpia el HTML eliminando estilos, scripts, formatos y atributos no deseados.
    """
    soup = BeautifulSoup(html, 'html.parser')

    # Eliminar estilos y scripts
    for tag in soup.find_all(['style', 'script']):
        tag.decompose()

    # Eliminar etiquetas de formato (font, span, b, i)
    for tag in soup.find_all(['font', 'span', 'b', 'i']):
        tag.unwrap()

    # Eliminar atributos de estilo, clase y alineación
    for tag in soup():
        if 'style' in tag.attrs:
            del tag.attrs['style']
        if 'class' in tag.attrs:
            del tag.attrs['class']
        if 'align' in tag.attrs:
            del tag.attrs['align']

    # Eliminar etiquetas vacías
    for tag in soup.find_all(True):
        if not tag.text.strip():
            tag.decompose()

    # Eliminar espacios innecesarios
    texto_limpio = re.sub(r'\s+', ' ', soup.get_text(separator=' ', strip=True))

    # Conservar títulos y listas (reconstruir HTML)
    html_limpio = str(soup) #Convertimos el soup a html
    return html_limpio

def procesar_archivos_html(carpeta_entrada, carpeta_salida):
    """
    Procesa los archivos HTML de la carpeta de entrada, los limpia y guarda
    los resultados en la carpeta de salida.
    """
    # Asegurarse de que la carpeta de textos limpios exista
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    # Iterar sobre todos los archivos en la carpeta HTML
    for nombre_archivo in os.listdir(carpeta_entrada):
        ruta_archivo = os.path.join(carpeta_entrada, nombre_archivo)

        # Verificar si el elemento en la carpeta es un archivo
        if os.path.isfile(ruta_archivo):
            try:
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
            except Exception as e:
                print(f"Error al procesar {nombre_archivo}: {e}")

    print("Proceso completado.")

# Rutas de las carpetas de entrada y salida
carpeta_html_entrada = '/ResultadosCJ/Procesados'
carpeta_textos_limpios_salida = '/ResultadosCJ/Limpios'

# Procesar archivos HTML
procesar_archivos_html(carpeta_html_entrada, carpeta_textos_limpios_salida)