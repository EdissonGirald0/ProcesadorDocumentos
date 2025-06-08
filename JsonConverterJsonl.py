import json
import os

# Configuración de rutas (puedes leerlas desde un archivo de configuración o argumentos de línea de comandos)
carpeta_json_entrada = '/home/dev1/AndroidStudioProjects/procesarDocument/CC_Autos_Div'
ruta_jsonl_salida = '/home/dev1/AndroidStudioProjects/procesarDocument/CC_Autos_Div/.jsonl'

# Lista para almacenar objetos JSON
datos_json = []

# Iterar sobre todos los archivos en la carpeta JSON
for nombre_archivo in os.listdir(carpeta_json_entrada):
    # Filtrar para incluir solo archivos JSON
    if nombre_archivo.endswith('.json'):
        ruta_archivo = os.path.join(carpeta_json_entrada, nombre_archivo)
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo_json:
                # Cargar el contenido del archivo JSON
                contenido_json = json.load(archivo_json)
                datos_json.append(contenido_json)
        except FileNotFoundError:
            print(f'Error: Archivo no encontrado: {ruta_archivo}')
        except json.JSONDecodeError:
            print(f'Error: Archivo JSON inválido: {ruta_archivo}')
        except IOError:
            print(f'Error: Error de E/S al leer el archivo: {ruta_archivo}')

# Escribir cada objeto JSON en una línea del archivo JSONL
try:
    with open(ruta_jsonl_salida, 'w', encoding='utf-8') as archivo_jsonl:
        for objeto_json in datos_json:
            # Utilizar el parámetro 'separators' para controlar el formato de salida
            json.dump(objeto_json, archivo_jsonl, ensure_ascii=False, separators=(',', ': '))
            archivo_jsonl.write('\n')  # Es necesario ya que el separador no lo incluye.
    print(f'Datos JSON convertidos a formato JSONL en: {ruta_jsonl_salida}')
except IOError:
    print(f'Error: Error de E/S al escribir en el archivo: {ruta_jsonl_salida}')