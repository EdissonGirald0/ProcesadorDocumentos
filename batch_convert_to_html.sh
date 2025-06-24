#!/bin/bash

###############################################################################
# Script para convertir archivos .pdf, .doc y .rtf a .html en lote.
# Autor: Edisson Giraldo        
# Fecha: 24/06/24
# Descripción:
#   Convierte archivos PDF a HTML usando pdftohtml,
#   archivos DOC a DOCX con LibreOffice y luego a HTML con Pandoc,
#   y archivos RTF a HTML con Pandoc.
#   Registra el resultado de cada conversión.
###############################################################################

# Configuración de rutas
INPUT_DIR="/home/dev1/Documents/documentosAltasCortes/consejo_judicatura/"
TEMP_DOCX_DIR="/home/dev1/AndroidStudioProjects/procesarDocument/TempDOCX/"
OUTPUT_DIR="/home/dev1/AndroidStudioProjects/procesarDocument/ResultadosCJ/Procesados/"
LOG_FILE="/home/dev1/AndroidStudioProjects/procesarDocument/registroSentenciasCJ.txt"

# Crear directorios de salida si no existen
mkdir -p "$TEMP_DOCX_DIR"
mkdir -p "$OUTPUT_DIR"

# Inicializar archivo de registro
echo "Archivos procesados correctamente:" > "$LOG_FILE"

# Función para convertir PDF a HTML
convert_pdf() {
    for file in "$INPUT_DIR"/*.pdf; do
        [ -f "$file" ] || continue
        pdftohtml -s -i "$file" "$OUTPUT_DIR/$(basename "$file" .pdf).html"
        if [ $? -eq 0 ]; then
            echo "$file" >> "$LOG_FILE"
        else
            echo "Error al procesar $file (pdftohtml)" >> "$LOG_FILE"
        fi
    done
}

# Función para convertir DOC a DOCX y luego a HTML
convert_doc() {
    for file in "$INPUT_DIR"/*.doc; do
        [ -f "$file" ] || continue
        libreoffice --headless --convert-to docx --outdir "$TEMP_DOCX_DIR" "$file"
        if [ $? -eq 0 ]; then
            DOCX_FILE="$TEMP_DOCX_DIR/$(basename "$file" .doc).docx"
            pandoc "$DOCX_FILE" -o "$OUTPUT_DIR/$(basename "$file" .doc).html"
            if [ $? -eq 0 ]; then
                echo "$file" >> "$LOG_FILE"
            else
                echo "Error al procesar $file (pandoc)" >> "$LOG_FILE"
            fi
        else
            echo "Error al procesar $file (libreoffice)" >> "$LOG_FILE"
        fi
    done
}

# Función para convertir RTF a HTML
convert_rtf() {
    for file in "$INPUT_DIR"/*.rtf; do
        [ -f "$file" ] || continue
        pandoc "$file" -o "$OUTPUT_DIR/$(basename "$file" .rtf).html"
        if [ $? -eq 0 ]; then
            echo "$file" >> "$LOG_FILE"
        else
            echo "Error al procesar $file (pandoc)" >> "$LOG_FILE"
        fi
    done
}

# Ejecutar conversiones
convert_pdf
convert_doc
convert_rtf

# Limpiar archivos temporales DOCX
rm -rf "$TEMP_DOCX_DIR"

echo "Conversión completada. Registro guardado en $LOG_FILE."#!/bin/bash

# Ruta al directorio que contiene los archivos .rtf, .doc y Pdf.
input_directory="/home/dev1/Documents/documentosAltasCortes/consejo_judicatura/"

# Ruta al directorio donde se guardarán los archivos DOCX temporales
temp_output_directory="/home/dev1/AndroidStudioProjects/procesarDocument/TempDOCX/"

# Ruta al directorio donde se guardarán los archivos HTML
output_directory="/home/dev1/AndroidStudioProjects/procesarDocument/ResultadosCJ/Procesados/"

# Ruta al archivo de registro
log_file="/home/dev1/AndroidStudioProjects/procesarDocument/registroSentenciasCJ.txt"

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
