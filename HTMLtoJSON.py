import os
import json
import pandas as pd
from pymongo import MongoClient

def convertir_a_json(html_folder, json_file):
    json_data = {"Sentencias": []}
    
    for nombre_archivo in os.listdir(html_folder):
        ruta_archivo = os.path.join(html_folder, nombre_archivo)

        if os.path.isfile(ruta_archivo) and nombre_archivo.endswith('_limpio.html'):
            # Obtener el nombre del archivo sin '_limpio.html'
            nombre_sin_extension = os.path.splitext(nombre_archivo)[0].replace('_limpio', '')
            
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido_html = archivo.read()
                documento = {"Sentencia_numero": nombre_sin_extension, "contenido": contenido_html}
                json_data["Sentencias"].append(documento)

    with open(json_file, 'w', encoding='utf-8') as json_output:
        json.dump(json_data, json_output, ensure_ascii=False, indent=2)

    print(f"Archivos HTML convertidos a JSON en '{json_file}'")

def exportar_a_csv(json_file, csv_file):
    df = pd.read_json(json_file)
    df.to_csv(csv_file, index=False, encoding='utf-8')
    print(f"Datos exportados a CSV en '{csv_file}'")

def insertar_en_mongodb(json_file, collection_name):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['tu_base_de_datos']
    collection = db[collection_name]

    with open(json_file, 'r', encoding='utf-8') as json_input:
        json_data = json.load(json_input)
        collection.insert_many(json_data["Autos"])

    print(f"Datos insertados en MongoDB en la colección '{collection_name}'")

# Rutas de archivos y carpetas
carpeta_textos_limpios = '/home/dev1/AndroidStudioProjects/procesarDocument/corteConsHTMLlimpio/autos/'
json_output_file = '/home/dev1/AndroidStudioProjects/procesarDocument/CC_Sentencias.json'
csv_output_file = '/home/dev1/AndroidStudioProjects/procesarDocument/CC_Sentencias.csv'
mongodb_collection_name = 'nombre_de_tu_coleccion_en_mongodb'

# Convertir a JSON
convertir_a_json(carpeta_textos_limpios, json_output_file)

# Opciones adicionales:
# 1. Exportar a CSV
exportar_a_csv(json_output_file, csv_output_file)

# 2. Insertar en MongoDB (asegúrate de tener MongoDB ejecutándose localmente)
# insertar_en_mongodb(json_output_file, mongodb_collection_name)


