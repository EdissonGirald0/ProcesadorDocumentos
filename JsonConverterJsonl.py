import json
import os
# Ruta de la carpeta que contiene los archivos JSON
carpeta_json_entrada = '/home/dev1/AndroidStudioProjects/procesarDocument/CC_Autos_Div'

# Ruta del archivo JSONL de salida
ruta_jsonl_salida = '/home/dev1/AndroidStudioProjects/procesarDocument/CC_Autos_Div/.jsonl'

# Lista para almacenar objetos JSON
datos_json = []

# Iterar sobre todos los archivos en la carpeta JSON
for nombre_archivo in os.listdir(carpeta_json_entrada):
    ruta_archivo = os.path.join(carpeta_json_entrada, nombre_archivo)

    # Verificar si el elemento en la carpeta es un archivo JSON
    if os.path.isfile(ruta_archivo) and nombre_archivo.endswith('.json'):
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo_json:
            # Cargar el contenido del archivo JSON
            contenido_json = json.load(archivo_json)
            datos_json.append(contenido_json)

# Escribir cada objeto JSON en una línea del archivo JSONL
with open(ruta_jsonl_salida, 'w', encoding='utf-8') as archivo_jsonl:
    for objeto_json in datos_json:
        json.dump(objeto_json, archivo_jsonl, ensure_ascii=False)
        archivo_jsonl.write('\n')

print(f'Datos JSON convertidos a formato JSONL en: {ruta_jsonl_salida}')
