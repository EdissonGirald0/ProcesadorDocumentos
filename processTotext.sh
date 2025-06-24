
#!/bin/bash

###############################################################################
# Script para convertir archivos PDF, DOC, DOCX y RTF a texto plano (.txt)
# Autor: Edisson Giraldo
# Fecha: 24/06/24
# Descripción:
#   Busca archivos en la carpeta de origen (y subcarpetas) y los convierte
#   a archivos .txt en la carpeta de destino, usando la herramienta adecuada.
###############################################################################

# Configuración de rutas
CARPETA_ORIGEN="/home/dev1/Documents/documentosAltasCortes/consejo_estado/"
CARPETA_DESTINO="/home/dev1/Documents/documentosAltasCortes/consejo_estado_text/"

# Crear la carpeta de destino si no existe
mkdir -p "$CARPETA_DESTINO"

# Función para convertir DOC a DOCX
convert_doc_to_docx() {
    local archivo_doc="$1"
    libreoffice --headless --convert-to docx --outdir "$(dirname "$archivo_doc")" "$archivo_doc"
    if [ $? -eq 0 ]; then
        echo "${archivo_doc}x"
    else
        echo ""
    fi
}

# Función para convertir archivo a texto
convert_to_text() {
    local archivo="$1"
    local destino="$2"
    case "$archivo" in
        *.pdf)
            pdftotext "$archivo" "$destino"
            ;;
        *.docx)
            docx2txt "$archivo" "$destino"
            ;;
        *.rtf)
            unrtf --text "$archivo" > "$destino"
            ;;
        *)
            echo "Extensión no compatible: $archivo"
            ;;
    esac
}

# Buscar y procesar archivos
find "$CARPETA_ORIGEN" -type f \( -iname "*.pdf" -o -iname "*.doc" -o -iname "*.docx" -o -iname "*.rtf" \) | while read -r ARCHIVO; do
    BASENAME="$(basename "${ARCHIVO%.*}").txt"
    DESTINO="$CARPETA_DESTINO/$BASENAME"

    # Si es DOC, convertir primero a DOCX
    if [[ "$ARCHIVO" == *.doc ]]; then
        NUEVO_DOCX="$(convert_doc_to_docx "$ARCHIVO")"
        if [ -n "$NUEVO_DOCX" ] && [ -f "$NUEVO_DOCX" ]; then
            convert_to_text "$NUEVO_DOCX" "$DESTINO"
        else
            echo "Error al convertir $ARCHIVO a DOCX"
        fi
    else
        convert_to_text "$ARCHIVO" "$DESTINO"
    fi
done

echo#!/bin/bash

# Ruta de la carpeta que contiene los archivos originales
CARPETA_ORIGEN="/home/dev1/Documents/documentosAltasCortes/consejo_estado/"

# Ruta de la carpeta donde se guardarán los archivos de texto resultantes
CARPETA_DESTINO="/home/dev1/Documents/documentosAltasCortes/consejo_estado_text/"

# Crear la carpeta de destino si no existe
mkdir -p "$CARPETA_DESTINO"

# Recorrer todos los archivos en la carpeta y subcarpetas
find "$CARPETA_ORIGEN" -type f \( -name "*.pdf" -o -name "*.doc" -o -name "*.docx" -o -name "*.rtf" \) |
while read ARCHIVO; do
    # Convertir el archivo DOC a formato DOCX si es necesario
    if [[ $ARCHIVO == *.doc ]]; then
        libreoffice --convert-to docx --outdir "$CARPETA_ORIGEN" "$ARCHIVO"
        ARCHIVO="${ARCHIVO}x"
    fi

    # Convertir el archivo y moverlo a la carpeta de destino
    case $ARCHIVO in
        *.pdf)
            pdftotext "$ARCHIVO" "$CARPETA_DESTINO/$(basename "${ARCHIVO%.*}").txt"
            ;;
        *.docx)
            docx2txt "$ARCHIVO" "$CARPETA_DESTINO/$(basename "${ARCHIVO%.*}").txt"
            ;;
        *.rtf)
            unrtf --text "$ARCHIVO" > "$CARPETA_DESTINO/$(basename "${ARCHIVO%.*}").txt"
            ;;
        *)
            echo "Extensión no compatible: $ARCHIVO"
            ;;
    esac
done
