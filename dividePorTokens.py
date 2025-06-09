import os
import json
from nltk.tokenize import word_tokenize

def dividir_json_por_tokens(json_file, output_folder, restriccion_tokens):
    """
    Divide a JSON file into multiple JSONL files based on a token count restriction.
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as json_input:
            data = json.load(json_input)["Sentencias"]
    except FileNotFoundError:
        print(f"Error: El archivo '{json_file}' no se encuentra.")
        return
    except json.JSONDecodeError:
        print(f"Error: El archivo '{json_file}' no es un JSON válido.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    jsonl_output_file = os.path.join(output_folder, 'Sentencias.jsonl')
    try:
        with open(jsonl_output_file, 'w', encoding='utf-8') as jsonl_output:
            total_tokens = 0
            for documento in data:
                # Tokenizar el contenido y contar tokens
                tokens = word_tokenize(documento["contenido"])
                num_tokens = len(tokens)

                # Verificar la restricción de tokens
                if total_tokens + num_tokens <= restriccion_tokens:
                    # Agregar el documento al archivo JSONL
                    json.dump(documento, jsonl_output, ensure_ascii=False)
                    jsonl_output.write('\n')
                    total_tokens += num_tokens
                else:
                    # Create a new file
                    jsonl_output.close()
                    jsonl_index = 1
                    jsonl_output_file = os.path.join(output_folder, f'Sentencias_{jsonl_index}.jsonl')
                    while os.path.exists(jsonl_output_file):
                        jsonl_index += 1
                        jsonl_output_file = os.path.join(output_folder, f'Sentencias_{jsonl_index}.jsonl')
                    with open(jsonl_output_file, 'w', encoding='utf-8') as jsonl_output:
                        json.dump(documento, jsonl_output, ensure_ascii=False)
                        jsonl_output.write('\n')
                        total_tokens = num_tokens

    except Exception as e:
        print(f"Error al escribir en el archivo JSONL: {e}")

    print(f"Archivos JSONL creados en '{output_folder}' con restricción de {restriccion_tokens} tokens")


# Rutas de archivos y carpetas
json_input_file = '/home/dev1/AndroidStudioProjects/procesarDocument/CC_Sentencias.json'
jsonl_output_folder = '/home/dev1/AndroidStudioProjects/procesarDocument/CC_Sentencias_Div/'

# Restricción de tokens
restriccion_de_tokens = 1999920

# Dividir el JSON según restricción de tokens
dividir_json_por_tokens(json_input_file, jsonl_output_folder, restriccion_de_tokens)