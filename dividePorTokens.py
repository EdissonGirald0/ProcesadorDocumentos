import os
import json
from nltk.tokenize import word_tokenize

def dividir_json_por_tokens(json_file, output_folder, restriccion_tokens):
    with open(json_file, 'r', encoding='utf-8') as json_input:
        data = json.load(json_input)["Sentencias"]

    total_tokens = 0
    json_index = 1
    jsonl_output_file = os.path.join(output_folder, f'Sentencias_{json_index}.jsonl')

    with open(jsonl_output_file, 'a', encoding='utf-8') as jsonl_output:
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
                # Cerrar el archivo actual y abrir uno nuevo para el próximo archivo JSONL
                jsonl_output.close()
                json_index += 1
                jsonl_output_file = os.path.join(output_folder, f'Sentencias_{json_index}.jsonl')
                with open(jsonl_output_file, 'a', encoding='utf-8') as jsonl_output:
                    json.dump(documento, jsonl_output, ensure_ascii=False)
                    jsonl_output.write('\n')
                total_tokens = num_tokens

    print(f"Archivos JSONL creados en '{output_folder}' con restricción de {restriccion_tokens} tokens")

# Rutas de archivos y carpetas
json_input_file = '/home/dev1/AndroidStudioProjects/procesarDocument/CC_Sentencias.json'
jsonl_output_folder = '/home/dev1/AndroidStudioProjects/procesarDocument/CC_Sentencias_Div/'

# Restricción de tokens
restriccion_de_tokens = 1999920

# Dividir el JSON según restricción de tokens
dividir_json_por_tokens(json_input_file, jsonl_output_folder, restriccion_de_tokens)
