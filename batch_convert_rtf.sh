#!/bin/bash

# Ruta al directorio que contiene los archivos .rtf, .doc y Pdf.
input_directory="/home/dev1/Documents/documentosAltasCortes/corte_suprema/"

# Ruta al directorio donde se guardarán los archivos DOCX temporales
temp_output_directory="/home/dev1/AndroidStudioProjects/procesarDocument/TempDOCX/"

# Ruta al directorio donde se guardarán los archivos HTML
output_directory="/home/dev1/AndroidStudioProjects/procesarDocument/ResultadosCSJ/ProcesadoSentencias/"

# Ruta al archivo de registro
log_file="/home/dev1/AndroidStudioProjects/procesarDocument/registroSentenciasCSJ.txt"

# Asegúrate de que los directorios de salida existan
mkdir -p "$temp_output_directory"
mkdir -p "$output_directory"

# Inicializa el archivo de registro
echo "Archivos procesados correctamente:" > "$log_file"

# Convierte todos los archivos .pdf a .html en el directorio de entrada
for file in "$input_directory"/*.pdf; do
    if [ -f "$file" ]; then
        # Utiliza pdftohtml para convertir el archivo .pdf a .html
        pdftohtml -s -i "$file" "$output_directory/$(basename "$file" .pdf).html"
        
        # Verifica si la conversión fue exitosa
        if [ $? -eq 0 ]; then
            echo "$file" >> "$log_file"
        else
            echo "Error al procesar $file (pdftohtml)" >> "$log_file"
        fi
    fi
done

# Convierte todos los archivos .doc a .docx en el directorio de entrada
for file in "$input_directory"/*.doc; do
    if [ -f "$file" ]; then
        # Utiliza libreoffice para convertir el archivo .doc a .docx
        libreoffice --headless --convert-to docx --outdir "$temp_output_directory" "$file"

        # Verifica si la conversión fue exitosa
        if [ $? -eq 0 ]; then
            # Utiliza pandoc para convertir el archivo .docx a .html
            pandoc "$temp_output_directory/$(basename "$file" .doc).docx" -o "$output_directory/$(basename "$file" .doc).html"
            
            # Verifica si la segunda conversión fue exitosa
            if [ $? -eq 0 ]; then
                echo "$file" >> "$log_file"
            else
                echo "Error al procesar $file (pandoc)" >> "$log_file"
            fi
        else
            echo "Error al procesar $file (libreoffice)" >> "$log_file"
        fi
    fi
done

# Convierte todos los archivos .rtf a .html en el directorio de entrada
for file in "$input_directory"/*.rtf; do
    if [ -f "$file" ]; then
        # Utiliza pandoc para convertir el archivo .rtf a .html
        pandoc "$file" -o "$output_directory/$(basename "$file" .rtf).html"
        
        # Verifica si la conversión fue exitosa
        if [ $? -eq 0 ]; then
            echo "$file" >> "$log_file"
        else
            echo "Error al procesar $file" >> "$log_file"
        fi
    fi
done

# Limpia los archivos temporales DOCX
rm -r "$temp_output_directory"

echo "Conversión completada. Registro guardado en $log_file."


#chmod +x batch_convert_rtf.sh
#./batch_convert_rtf.sh
