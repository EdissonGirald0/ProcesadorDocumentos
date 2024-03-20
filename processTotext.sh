
#!/bin/bash

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
