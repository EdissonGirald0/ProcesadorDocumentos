import os
import json
import pandas as pd
from pymongo import MongoClient

def convertir_a_json(html_folder, json_file):
    """
    Converts HTML files from a directory to a JSON file.
    """
    json_data = {"Sentencias": []}

    for nombre_archivo in os.listdir(html_folder):
        ruta_archivo = os.path.join(html_folder, nombre_archivo)
        if os.path.isfile(ruta_archivo) and nombre_archivo.endswith('_limpio.html'):
            nombre_sin_extension = os.path.splitext(nombre_archivo)[0].replace('_limpio', '')

            try:
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                    contenido_html = archivo.read()
                    documento = {"Sentencia_numero": nombre_sin_extension, "contenido": contenido_html}
                    json_data["Sentencias"].append(documento)
            except Exception as e:
                print(f"Error al procesar {nombre_archivo}: {e}")

    try:
        with open(json_file, 'w', encoding='utf-8') as json_output:
            json.dump(json_data, json_output, ensure_ascii=False, indent=2)
        print(f"Archivos HTML convertidos a JSON en '{json_file}'")
    except Exception as e:
        print(f"Error al escribir el archivo JSON: {e}")

def exportar_a_csv(json_file, csv_file):
    """
    Exports JSON data to a CSV file.
    """
    try:
        df = pd.read_json(json_file)
        df.to_csv(csv_file, index=False, encoding='utf-8')
        print(f"Datos exportados a CSV en '{csv_file}'")
    except Exception as e:
        print(f"Error al exportar a CSV: {e}")

def insertar_en_mongodb(json_file, collection_name, mongodb_uri="mongodb://localhost:27017/"):
    """
    Inserts JSON data into a MongoDB collection.
    """
    try:
        client = MongoClient(mongodb_uri)
        db = client['tu_base_de_datos']
        collection = db[collection_name]

        with open(json_file, 'r', encoding='utf-8') as json_input:
            json_data = json.load(json_input)
            collection.insert_many(json_data["Sentencias"]) # Fixed the key
        print(f"Datos insertados en MongoDB en la colección '{collection_name}'")
    except Exception as e:
        print(f"Error al insertar en MongoDB: {e}")

# Rutas de archivos y carpetas
carpeta_textos_limpios = '/home/dev1/AndroidStudioProjects/procesarDocument/ResultadosCJ/Limpios'
json_output_file = '/home/dev1/AndroidStudioProjects/procesarDocument/ResultadosCJ/Jsons/CJ_todos.json'
csv_output_file = '/home/dev1/AndroidStudioProjects/procesarDocument/ResultadosCJ/Jsons/CJ_Todas.csv'
mongodb_collection_name = 'nombre_de_tu_coleccion_en_mongodb'
mongodb_uri = "mongodb://localhost:27017/"

# Convertir a JSON
convertir_a_json(carpeta_textos_limpios, json_output_file)

# Opciones adicionales:
# 1. Exportar a CSV
exportar_a_csv(json_output_file, csv_output_file)

# 2. Insertar en MongoDB (asegúrate de tener MongoDB ejecutándose localmente)
insertar_en_mongodb(json_output_file, mongodb_collection_name, mongodb_uri)

