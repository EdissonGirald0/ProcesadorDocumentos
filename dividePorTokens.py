import os
import json
from nltk.tokenize import word_tokenize

def dividir_json_por_tokens(json_file, output_folder, restriccion_tokens):
    with open(json_file, 'r', encoding='utf-8') as json_input:
        data = json.load(json_input)

    total_tokens = 0
    json_index = 1
    json_data = {"Sentencias": []}

    for documento in data["Sentencias"]:
        # Tokenizar el contenido y contar tokens
        tokens = word_tokenize(documento["contenido"])
        num_tokens = len(tokens)

        # Verificar la restricción de tokens
        if total_tokens + num_tokens <= restriccion_tokens:
            # Agregar el documento al JSON
            json_data["Sentencias"].append(documento)
            total_tokens += num_tokens
        else:
            # Guardar JSON y reiniciar para el próximo archivo
            json_output_file = os.path.join(output_folder, f'Sentencias_{json_index}.json')
            with open(json_output_file, 'w', encoding='utf-8') as json_output:
                json.dump(json_data, json_output, ensure_ascii=False, indent=2)
            print(f"Archivo JSON '{json_output_file}' creado con restricción de {restriccion_tokens} tokens")

            # Reiniciar variables
            total_tokens = num_tokens
            json_index += 1
            json_data = {"Sentencias": [documento]}

    # Guardar el último JSON si quedan documentos
    if json_data["Sentencias"]:
        json_output_file = os.path.join(output_folder, f'Sentencias_{json_index}.json')
        with open(json_output_file, 'w', encoding='utf-8') as json_output:
            json.dump(json_data, json_output, ensure_ascii=False, indent=2)
        print(f"Archivo JSON '{json_output_file}' creado con restricción de {restriccion_tokens} tokens")

# Rutas de archivos y carpetas
json_input_file = '/home/dev1/AndroidStudioProjects/procesarDocument/CC_Sentencias.json'
json_output_folder = '/home/dev1/AndroidStudioProjects/procesarDocument/CC_Sentencias_Div/'

# Restricción de tokens
restriccion_de_tokens = 2000000

# Dividir el JSON según restricción de tokens
dividir_json_por_tokens(json_input_file, json_output_folder, restriccion_de_tokens)
